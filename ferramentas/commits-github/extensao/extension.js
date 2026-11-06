// Commits do GitHub na barra de cima: roda ~/.local/bin/github-commits --json a cada 5 min
// e ao abrir o menu. No painel: commits de hoje e dias seguidos. No menu: grade igual à do
// perfil do GitHub (colunas = semanas) e os últimos commits.
import GLib from 'gi://GLib';
import Gio from 'gi://Gio';
import GObject from 'gi://GObject';
import St from 'gi://St';
import Clutter from 'gi://Clutter';
import {Extension} from 'resource:///org/gnome/shell/extensions/extension.js';
import * as Main from 'resource:///org/gnome/shell/ui/main.js';
import * as PanelMenu from 'resource:///org/gnome/shell/ui/panelMenu.js';
import * as PopupMenu from 'resource:///org/gnome/shell/ui/popupMenu.js';

const SCRIPT = GLib.build_filenamev([GLib.get_home_dir(), '.local', 'bin', 'github-commits']);
const INTERVALO = 300;
const COR = {ok: '#39d353', alerta: '#f0c060', critico: '#ff6b6b'};
const DIM = 'color: rgba(255,255,255,0.6);';
const LADO = 13; // tamanho do quadradinho
const VAO = 3; // espaço entre quadradinhos
const NOMES_LINHAS = ['', 'seg', '', 'qua', '', 'sex', '']; // linhas: dom a sáb, como no GitHub

// cor do quadradinho conforme a quantidade de commits no dia
const NIVEIS = ['rgba(255,255,255,0.10)', '#0e4429', '#006d32', '#26a641', '#39d353'];
function corDoDia(n) {
    if (n <= 0)
        return NIVEIS[0];
    if (n === 1)
        return NIVEIS[1];
    if (n <= 3)
        return NIVEIS[2];
    if (n <= 6)
        return NIVEIS[3];
    return NIVEIS[4];
}

function rotulo(text, style = '') {
    return new St.Label({text, style, y_align: Clutter.ActorAlign.CENTER});
}

function quadrado(cor, lado, extra = '') {
    return new St.Widget({
        width: lado, height: lado,
        y_align: Clutter.ActorAlign.CENTER,
        style: `background-color: ${cor}; border-radius: 3px; ${extra}`,
    });
}

function pequeno(text, largura) {
    return new St.Label({text, width: largura, style: `${DIM} font-size: 0.75em;`});
}

// grade: uma coluna por semana, e uma linha de meses em cima
function montarGrade(semanas) {
    const passo = LADO + VAO;
    const caixa = new St.BoxLayout({orientation: Clutter.Orientation.VERTICAL, style: `spacing: ${VAO}px;`});

    // meses: cada nome ocupa da coluna em que o mês começa até a próxima
    const meses = new St.BoxLayout();
    meses.add_child(pequeno('', 30));
    let i = 0;
    while (i < semanas.length) {
        let fim = i + 1;
        while (fim < semanas.length && !semanas[fim].mes)
            fim++;
        meses.add_child(pequeno(semanas[i].mes, passo * (fim - i)));
        i = fim;
    }
    caixa.add_child(meses);

    const corpo = new St.BoxLayout({style: `spacing: ${VAO}px;`});
    const nomes = new St.BoxLayout({orientation: Clutter.Orientation.VERTICAL, style: `spacing: ${VAO}px;`});
    for (const nome of NOMES_LINHAS) {
        const l = pequeno(nome, 27);
        l.height = LADO;
        nomes.add_child(l);
    }
    corpo.add_child(nomes);
    for (const semana of semanas) {
        const coluna = new St.BoxLayout({orientation: Clutter.Orientation.VERTICAL, style: `spacing: ${VAO}px;`});
        for (const dia of semana.dias) {
            if (dia.futuro) {
                coluna.add_child(quadrado('transparent', LADO));
                continue;
            }
            const borda = dia.hoje ? 'border: 1px solid rgba(255,255,255,0.85);' : '';
            coluna.add_child(quadrado(corDoDia(dia.n), LADO, borda));
        }
        corpo.add_child(coluna);
    }
    caixa.add_child(corpo);

    // legenda: menos ▢▢▢▢▢ mais
    const legenda = new St.BoxLayout({style: `spacing: ${VAO}px; margin-top: 4px;`, x_align: Clutter.ActorAlign.END});
    legenda.add_child(rotulo('menos', `${DIM} font-size: 0.75em; margin-right: 2px;`));
    for (const cor of NIVEIS)
        legenda.add_child(quadrado(cor, 10));
    legenda.add_child(rotulo('mais', `${DIM} font-size: 0.75em; margin-left: 2px;`));
    caixa.add_child(legenda);
    return caixa;
}

const Indicador = GObject.registerClass(
class Indicador extends PanelMenu.Button {
    _init() {
        super._init(0.0, 'Commits do GitHub');
        this._painel = new St.BoxLayout({style: 'spacing: 5px;', y_align: Clutter.ActorAlign.CENTER});
        this._painel.add_child(rotulo('Git …'));
        this.add_child(this._painel);
        this.menu.connect('open-state-changed', (_m, aberto) => {
            if (aberto)
                this.atualizar();
        });
    }

    atualizar() {
        if (this._rodando)
            return;
        this._rodando = true;
        try {
            const proc = Gio.Subprocess.new([SCRIPT, '--json'],
                Gio.SubprocessFlags.STDOUT_PIPE | Gio.SubprocessFlags.STDERR_SILENCE);
            proc.communicate_utf8_async(null, null, (p, res) => {
                this._rodando = false;
                if (this._fechado)
                    return;
                try {
                    const [, out] = p.communicate_utf8_finish(res);
                    const d = JSON.parse(out);
                    if (d.erro)
                        this._falha(d.erro);
                    else
                        this._mostrar(d);
                } catch (e) {
                    this._falha(String(e));
                }
            });
        } catch (e) {
            this._rodando = false;
            this._falha('Script não encontrado');
        }
    }

    _falha(msg) {
        this._painel.destroy_all_children();
        this._painel.add_child(rotulo('Git ?', DIM));
        this.menu.removeAll();
        this.menu.addMenuItem(new PopupMenu.PopupMenuItem(msg, {reactive: false}));
        const botao = new PopupMenu.PopupMenuItem('Tentar de novo');
        botao.connect('activate', () => this.atualizar());
        this.menu.addMenuItem(botao);
    }

    _mostrar(d) {
        const seq = `${d.sequencia}${d.sequencia_mais ? '+' : ''}`;

        // painel: "Git ■ 3  🔥 5"
        this._painel.destroy_all_children();
        this._painel.add_child(rotulo('Git', DIM));
        this._painel.add_child(quadrado(COR[d.nivel] ?? COR.ok, 9));
        this._painel.add_child(rotulo(`${d.hoje}`, 'font-weight: bold;'));
        this._painel.add_child(rotulo(`🔥${seq}`, 'margin-left: 4px;'));

        this.menu.removeAll();
        this.menu.addMenuItem(new PopupMenu.PopupSeparatorMenuItem(`GitHub · @${d.login}`));

        // resumo
        const resumo = new PopupMenu.PopupBaseMenuItem({reactive: false});
        const col = new St.BoxLayout({orientation: Clutter.Orientation.VERTICAL, style: 'spacing: 3px;'});
        const textoHoje = d.hoje
            ? `Hoje: ${d.hoje} commit${d.hoje > 1 ? 's' : ''} ✔`
            : 'Hoje: nenhum commit ainda';
        col.add_child(rotulo(textoHoje, `font-weight: bold; color: ${COR[d.nivel] ?? COR.ok};`));
        col.add_child(rotulo(`Sequência: ${seq} dia${d.sequencia === 1 ? '' : 's'} seguidos`));
        col.add_child(rotulo(`Últimos 7 dias: ${d.semana} commits`, DIM));
        col.add_child(rotulo(`3 meses: ${d.periodo} commits em ${d.dias_com_commit} dias`, DIM));
        resumo.add_child(col);
        this.menu.addMenuItem(resumo);

        const cal = new PopupMenu.PopupBaseMenuItem({reactive: false});
        cal.add_child(montarGrade(d.grade));
        this.menu.addMenuItem(cal);

        // últimos commits (clicar abre no GitHub)
        this.menu.addMenuItem(new PopupMenu.PopupSeparatorMenuItem('Últimos commits'));
        if (!d.ultimos.length)
            this.menu.addMenuItem(new PopupMenu.PopupMenuItem('Nenhum commit recente', {reactive: false}));
        for (const c of d.ultimos) {
            const item = new PopupMenu.PopupBaseMenuItem();
            const box = new St.BoxLayout({orientation: Clutter.Orientation.VERTICAL, style: 'spacing: 2px;'});
            const msg = c.msg.length > 48 ? `${c.msg.slice(0, 47)}…` : c.msg;
            box.add_child(rotulo(msg));
            box.add_child(rotulo(`${c.repo}  ·  ${c.quando}`, `${DIM} font-size: 0.85em;`));
            item.add_child(box);
            item.connect('activate', () => Gio.AppInfo.launch_default_for_uri(c.url, null));
            this.menu.addMenuItem(item);
        }

        this.menu.addMenuItem(new PopupMenu.PopupSeparatorMenuItem());
        const perfil = new PopupMenu.PopupMenuItem('Abrir meu perfil no GitHub');
        perfil.label.style = 'font-size: 0.9em;';
        perfil.connect('activate', () => Gio.AppInfo.launch_default_for_uri(d.perfil, null));
        this.menu.addMenuItem(perfil);
        const botao = new PopupMenu.PopupMenuItem(`Atualizar agora  ·  lido às ${d.hora}`);
        botao.connect('activate', () => this.atualizar());
        this.menu.addMenuItem(botao);
    }

    destroy() {
        this._fechado = true;
        super.destroy();
    }
});

export default class CommitsGitHub extends Extension {
    enable() {
        this._indicador = new Indicador();
        Main.panel.addToStatusArea(this.uuid, this._indicador, 1, 'right');
        this._indicador.atualizar();
        this._timer = GLib.timeout_add_seconds(GLib.PRIORITY_DEFAULT, INTERVALO, () => {
            this._indicador.atualizar();
            return GLib.SOURCE_CONTINUE;
        });
    }

    disable() {
        if (this._timer) {
            GLib.source_remove(this._timer);
            this._timer = null;
        }
        this._indicador?.destroy();
        this._indicador = null;
    }
}
