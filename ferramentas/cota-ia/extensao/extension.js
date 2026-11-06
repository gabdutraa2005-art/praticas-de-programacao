// Cota de IA na barra de cima: roda ~/.local/bin/claude-cota --json a cada 3 min
// e ao abrir o menu. Mini-barras no painel, detalhe e renovação no menu.
import GLib from 'gi://GLib';
import Gio from 'gi://Gio';
import GObject from 'gi://GObject';
import St from 'gi://St';
import Clutter from 'gi://Clutter';
import {Extension} from 'resource:///org/gnome/shell/extensions/extension.js';
import * as Main from 'resource:///org/gnome/shell/ui/main.js';
import * as PanelMenu from 'resource:///org/gnome/shell/ui/panelMenu.js';
import * as PopupMenu from 'resource:///org/gnome/shell/ui/popupMenu.js';

const SCRIPT = GLib.build_filenamev([GLib.get_home_dir(), '.local', 'bin', 'claude-cota']);
const INTERVALO = 180;
const COR = {ok: '#8fd19e', alerta: '#f0c060', critico: '#ff6b6b'};
const DIM = 'color: rgba(255,255,255,0.6);';

function barra(pct, nivel, largura, altura) {
    const trilho = new St.Widget({
        layout_manager: new Clutter.BinLayout(),
        width: largura, height: altura,
        y_align: Clutter.ActorAlign.CENTER,
        style: `background-color: rgba(255,255,255,0.18); border-radius: ${altura / 2}px;`,
    });
    const cheio = Math.round(largura * Math.min(100, Math.max(0, pct)) / 100);
    if (cheio > 0) {
        trilho.add_child(new St.Widget({
            width: Math.max(cheio, altura), height: altura,
            x_align: Clutter.ActorAlign.START, x_expand: true,
            style: `background-color: ${COR[nivel] ?? COR.ok}; border-radius: ${altura / 2}px;`,
        }));
    }
    return trilho;
}

function rotulo(text, style = '') {
    return new St.Label({text, style, y_align: Clutter.ActorAlign.CENTER});
}

const Indicador = GObject.registerClass(
class Indicador extends PanelMenu.Button {
    _init() {
        super._init(0.0, 'Cota de IA');
        this._painel = new St.BoxLayout({style: 'spacing: 5px;', y_align: Clutter.ActorAlign.CENTER});
        this._painel.add_child(rotulo('IA …'));
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
                    this._mostrar(JSON.parse(out));
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
        this._painel.add_child(rotulo('IA ?', DIM));
        this.menu.removeAll();
        this.menu.addMenuItem(new PopupMenu.PopupMenuItem(msg, {reactive: false}));
    }

    _mostrar(d) {
        this._painel.destroy_all_children();
        this.menu.removeAll();

        d.provedores.forEach((p, i) => {
            // painel: "Claude ▬ 35% ▬ 59%"
            const grupo = new St.BoxLayout({style: `spacing: 4px; ${i ? 'margin-left: 10px;' : ''}`});
            grupo.add_child(rotulo(p.nome, DIM));
            if (p.erro || !p.janelas.length)
                grupo.add_child(rotulo('?', DIM));
            for (const j of p.janelas) {
                grupo.add_child(barra(j.pct, j.nivel, 26, 6));
                grupo.add_child(rotulo(`${j.pct}%`, 'font-weight: bold;'));
            }
            this._painel.add_child(grupo);

            // menu: um bloco por provedor
            this.menu.addMenuItem(new PopupMenu.PopupSeparatorMenuItem(`${p.nome} ${p.plano}`.trim()));
            if (p.erro)
                this.menu.addMenuItem(new PopupMenu.PopupMenuItem(p.erro, {reactive: false}));
            for (const j of p.janelas) {
                const item = new PopupMenu.PopupBaseMenuItem({reactive: false});
                const col = new St.BoxLayout({orientation: Clutter.Orientation.VERTICAL, style: 'spacing: 4px;', x_expand: true});
                const topo = new St.BoxLayout({style: 'spacing: 8px;'});
                topo.add_child(rotulo(j.rotulo === '5h' ? 'Sessão 5h' : 'Semana', 'min-width: 70px;'));
                topo.add_child(barra(j.pct, j.nivel, 180, 8));
                topo.add_child(rotulo(`${j.pct}%`, `font-weight: bold; color: ${COR[j.nivel] ?? COR.ok};`));
                col.add_child(topo);
                col.add_child(rotulo(j.detalhe, `${DIM} font-size: 0.85em;`));
                item.add_child(col);
                this.menu.addMenuItem(item);
            }
            const abrir = new PopupMenu.PopupMenuItem(`Abrir página de uso do ${p.nome}`);
            abrir.label.style = 'font-size: 0.9em;';
            abrir.connect('activate', () => Gio.AppInfo.launch_default_for_uri(p.url, null));
            this.menu.addMenuItem(abrir);
        });

        this.menu.addMenuItem(new PopupMenu.PopupSeparatorMenuItem());
        const botao = new PopupMenu.PopupMenuItem(`Atualizar agora  ·  lido às ${d.hora}`);
        botao.connect('activate', () => this.atualizar());
        this.menu.addMenuItem(botao);
    }

    destroy() {
        this._fechado = true;
        super.destroy();
    }
});

export default class CotaIA extends Extension {
    enable() {
        this._indicador = new Indicador();
        Main.panel.addToStatusArea(this.uuid, this._indicador, 0, 'right');
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
