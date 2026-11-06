# Ferramentas da barra do Linux

Duas ferramentas que rodam na barra de cima do meu Ubuntu (GNOME). Estão aqui para estudo:
ler, mexer e entender aos poucos.

| Pasta | O que mostra na barra |
|---|---|
| `commits-github/` | commits de hoje, dias seguidos (🔥) e a grade de quadradinhos do GitHub |
| `cota-ia/` | quanto já usei das cotas de 5 horas e da semana do Claude e do Codex |

## Como cada uma funciona

As duas têm o mesmo desenho, em duas partes:

1. **Um script em Python** (`.py`) busca os dados na internet e imprime o resultado.
   - Sem nada: imprime um resumo para gente ler.
   - Com `--json`: imprime em JSON, para a extensão ler.
2. **Uma extensão do GNOME** (`extensao/extension.js`, em JavaScript) roda o script de tempos em
   tempos, lê o JSON e desenha na barra.

Testar o script sozinho, no terminal:

```bash
python3 commits-github/github_commits.py
python3 commits-github/github_commits.py --json
```

## Estas cópias não mexem na barra

O que roda de verdade fica em `~/.local/bin/` e em `~/.local/share/gnome-shell/extensions/`.
Os arquivos daqui são cópias: posso mudar e quebrar à vontade sem estragar nada.

## O que estudar em cada uma, conforme o roadmap

- **Já dá para reconhecer (Mundo 1 e 2):** variáveis, `if`/`elif`/`else`, `print` com f-string,
  `while` (a contagem da sequência em `github_commits.py`).
- **Mundo 3:** listas, dicionários, funções (`def`), `try`/`except`, `import`.
- **Depois:** JSON, APIs e HTTP (o `pegar()` da cota), datas com `datetime`, e o JavaScript da extensão.

Primeiro desafio sugerido: em `github_commits.py`, achar a linha que decide se o quadradinho da
barra fica verde, amarelo ou vermelho, e trocar a hora do vermelho de 21h para 20h.
