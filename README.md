# Práticas de Programação

Meus estudos de programação, do zero.

**Objetivos:** cursar Engenharia de Software e entender o hub que estou construindo para a minha empresa (React, Vite, TypeScript e PostgreSQL).

## Pastas

- `Python/`: exercícios do Curso em Vídeo e desafios extras
- `JS/` e `Ts/`: JavaScript e TypeScript
- `LIVE CODING/`: anotações de lives
- `github/`: anotações de Git

## Plano de estudos

Ordem pensada para, no fim, conseguir ler o hub de ponta a ponta.

**1. Python (agora)**
- [ ] Mundo 1: fundamentos
- [ ] Mundo 2: `if`, `for`, `while`

**2. Python, parte 2**
- [ ] Mundo 3: listas, dicionários, funções, módulos e exceções
- [ ] Expressões regulares (`re`) e testes com `unittest`

**3. HTML e CSS (primeiros projetos)**
- [ ] HTML: estrutura da página
- [ ] CSS: visual

**4. Banco de dados**
- [ ] SQL e PostgreSQL: `SELECT`, `WHERE`, `JOIN`, `GROUP BY`

**5. Web (para o hub)**
- [ ] JavaScript: comportamento, JSON e `async`/`await`
- [ ] HTTP e APIs: `GET`, `POST` e códigos de resposta
- [ ] Node e npm
- [ ] TypeScript: JS com tipos
- [ ] Zod: conferir o formato dos dados
- [ ] React + Vite + Tailwind: telas em componentes

**6. Depois**
- [ ] Testes automatizados e Docker
- [ ] Desafios da pasta `Python/Desafios/`
- [ ] CS50 (Harvard)

## Para corrigir

- [ ] `Aula 08 18 .py`: trocar `maht` por `math`
- [ ] `Desafios par3 .py`: tirar o `s` de dentro das aspas
- [ ] `ola.py`: trocar `input` por `print`
- [ ] `Desafios aula 04 par 2 .py`: refazer no Mundo 2
- [ ] `Aula 07 09 .py`: refazer a tabuada com `for`
- [ ] Anotações: fatiamento usa `[ ]`, `float` e `title()`

## Hábitos

- Nomes claros: `preco`, não `p`
- Arquivos sem espaço: `aula08_desafio018.py`
- Rodar o código antes do commit
- Ler a mensagem de erro inteira
- Live ajuda, mas praticar é o que ensina

## Git

```bash
git add -A
git commit -m "o que eu fiz"
git push
```

Nada sobe sozinho: só vai para o GitHub o que passou por esses comandos.

**Renomear o último commit** (antes do `push`):

```bash
git commit --amend -m "nova mensagem"
```

Commit que já foi para o GitHub: não renomear, só acertar nos próximos.

**Boas mensagens** começam com um verbo e dizem o que foi feito:

- ✅ `Adiciona exercícios da aula 09`
- ❌ `teste`, `ajustes`

## Materiais

- [Curso em Vídeo](https://www.cursoemvideo.com/)
- [CS50](https://cs50.harvard.edu/x/)
- [30 Days of Python](https://github.com/Asabeneh/30-Days-Of-Python)
- [30 Days of JavaScript](https://github.com/Asabeneh/30-Days-Of-JavaScript)


git clone https://github.com/gabdutraa2005-art/NOME-DO-REPO.git
cd NOME-DO-REPO
PARA PUXAR REPO DO GIT

>>> ou ...: você está no Python, que aceita código, mas não comandos como git ou cd.
$: você está no terminal normal.

git status
git pull origin main
 # Esse comando serve para puxar direto do git as atualizações

git add .
git commit -m "sua mensagem"
git pull origin main
