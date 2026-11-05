# Roadmap · do zero até ler o Hub

Montado em 03/11/2026, a partir do código do Hub nessa data e do plano que está no README do repositório `praticas-de-programacao`. Os prazos estão em **horas de estudo**. Para saber em quantas semanas chegas a cada nível, divide as horas pelas horas que estudas por semana.

Fica fora do repositório de propósito: o repositório é público e este arquivo fala do Hub.

## Veredito

**A direção do teu plano está certa.** HTML, CSS, JavaScript, TypeScript, React e SQL são exatamente o que o Hub usa. Mas ele precisa de três ajustes:

1. **Faltam peças que o Hub usa em todo lugar:** HTTP e APIs, Node e npm, `async`/`await`, Zod, testes, permissões no banco (RLS) e Docker.
2. **Angular, Kafka e Spring Boot não aparecem no Hub.** Adia esses três (ver "O que sai do plano").
3. **O Mundo 3 do Python vem antes do JavaScript, e não depois.** Funções, listas, dicionários e exceções valem em qualquer linguagem, e as automações do Hub em Python são o primeiro código dele que tu vais conseguir ler.

**A meta não é ler o Hub inteiro.** Ele tem uns 210 mil linhas e cresce toda semana. A meta é pegar **uma fatia** (uma função do sistema, como o mural de avisos) e seguir ela de ponta a ponta. Isso é possível porque todos os módulos repetem o mesmo desenho: quem aprende um consegue ler os outros. E os comentários do código estão em português e explicam o porquê, o que ajuda muito.

## O que o Hub usa

| Peça | Onde fica no Hub | Tamanho aprox. | No teu plano? |
|---|---|---|---|
| React + Vite + Tailwind (TypeScript) | `frontend/` | 87 mil linhas | ✅ |
| Fastify, um servidor de API (TypeScript) | `backend/` | 54 mil linhas | Em parte: falta HTTP, APIs e Node |
| Zod, que confere se um dado tem o formato certo | `shared/` | 18 mil linhas | ❌ |
| SQL e Postgres (Supabase), com RLS | `banco/` | 20 mil linhas | SQL ✅ · RLS ❌ |
| Python | `automacoes/` | 12 mil linhas | ✅ (precisa do Mundo 3) |
| Testes (Vitest e Playwright) | arquivos `.test.ts` e `e2e/` | em quase todas as pastas | ❌ |
| Docker, terminal e Git | para rodar e versionar | | Git ✅ · Docker ❌ |

## Os 5 níveis de leitura

Os caminhos dos arquivos partem da pasta `PROJETO INTERNO AVT`.

| Nível | Tu consegues… | Horas de estudo até lá (aprox.) |
|---|---|---|
| 1 · Mapa | dizer o que cada pasta faz | já |
| 2 · Python do Hub | ler uma automação | 80 a 100 h |
| 3 · Banco | ler uma tabela e dizer quem pode ver os dados | 130 a 160 h |
| 4 · Fatia inteira | seguir um clique da tela até o banco | 260 a 320 h |
| 5 · Revisão | olhar uma mudança feita pela IA e julgar | contínuo, depois do 4 |

Exemplo: com 1h por dia (7h por semana), o Nível 4 chega em uns 9 a 11 meses. Com 3h por semana, em uns 20 a 24.

### Nível 1 · Mapa (dá para começar já)

- **Estudar:** nada novo. Só ler.
- **Ler:** `README.md`, `discussoes/01-visao-geral.md`, `discussoes/03-areas-e-modulos.md` e `discussoes/09-onde-estamos.md`.
- **Marco:** explicar, com as tuas palavras e em uma linha cada, o que fazem `frontend/`, `backend/`, `shared/`, `banco/` e `automacoes/`.

### Nível 2 · Python do Hub

- **Estudar:** Mundo 2 e Mundo 3 (funções, listas, dicionários, módulos, exceções), mais o básico de expressões regulares (`re`) e de testes com `unittest`.
- **Marco 1:** explicar `automacoes/tiny/erros.py`, que tem 57 linhas.
- **Marco 2:** explicar `automacoes/relatorio_de_erros/limpeza.py`: o que entra, o que sai e por que existe.

### Nível 3 · Banco

- **Estudar:** SQL (`SELECT`, `WHERE`, `JOIN`, `GROUP BY`, `INSERT`), chave primária e estrangeira, e a ideia de permissão por linha (RLS).
- **Marco:** em `banco/supabase/migrations/20261005131016_avisos.sql`, dizer que colunas a tabela de avisos tem e quem pode ler um aviso.

### Nível 4 · Uma fatia de ponta a ponta

- **Estudar, nesta ordem:**
  1. JavaScript, com JSON e `async`/`await`.
  2. HTTP: `GET`, `POST` e os códigos 403, 404 e 409.
  3. Node e npm.
  4. TypeScript.
  5. Zod.
  6. React.
- **Marco:** seguir o mural de avisos, de ponta a ponta, explicando o que cada arquivo faz:
  1. A tela: `frontend/src/base/avisos/PaginaAvisos.tsx`.
  2. O hook que busca os dados: `frontend/src/dados/avisos/useAvisos.ts`.
  3. O contrato entre a tela e a API: `shared/src/contratos/avisos.ts`.
  4. A API: `backend/src/modulos/avisos/rotas.ts`, depois `servico.ts`, depois `repositorio.ts`.
  5. A tabela do Nível 3.

### Nível 5 · Revisar o que a IA faz

- **Estudar:** testes (Vitest), Docker básico, `git diff` e `git log`.
- **Marco:** pegar uma mudança recente do Hub e responder três perguntas: o que mudou, por que mudou, e se veio com teste.

## A ordem dos estudos (uma lista só)

1. Python Mundo 2 (agora) e o projeto 1 do portfólio.
2. Python Mundo 3, `re` e `unittest`. Fecha o **Nível 2**.
3. HTML e CSS, com as landing pages (projetos 3 a 5 do portfólio).
4. SQL. Fecha o **Nível 3**.
5. JavaScript, depois HTTP e APIs, depois Node e npm.
6. TypeScript e Zod.
7. React, com Vite e Tailwind. Fecha o **Nível 4**.
8. Testes e Docker. Abre o **Nível 5**.
9. Os 5 itens do **Nível 6 · Mercado** (abaixo). A lógica (item 1 de lá) começa já, junto com o Python.

## Nível 6 · Mercado (estágio, depois empresa grande)

Acrescentado em 05/11/2026. Meta: primeiro um estágio e depois CLT numa empresa grande. Os níveis 1 a 5 ensinam a **ler**; este ensina a **escrever** o que um processo seletivo cobra.

1. **Lógica e estruturas de dados:** listas, dicionários, busca e ordenação. Treinar com exercícios fáceis no Beecrowd ou no LeetCode, que é o que cai em teste técnico de estágio. Começa já, em paralelo com o Mundo 2.
2. **Uma API tua, feita do zero:** cadastro, login e CRUD com banco, sem copiar do Hub. Depois do Nível 4.
3. **Deploy:** colocar essa API e uma tela no ar, com link para mostrar.
4. **Git de verdade:** branch, pull request e commits frequentes no GitHub.
5. **Inglês técnico:** pelo menos para ler documentação e mensagens de erro.

**Marco:** a API do item 2 no ar, com README, e tu explicando o código sem olhar.

**Empresa grande e Java:** muitas empresas grandes (bancos, varejo, seguradoras) usam Java com Spring Boot no backend. Depois que a tua API em TypeScript estiver pronta, refazer a mesma API em Java é o melhor jeito de aprender Spring, porque tu já conheces o problema e só muda a linguagem.

O Nível 1 e o hábito do termo da semana (abaixo) correm em paralelo, desde já.

## O que sai do plano, por enquanto

- **Angular:** faz o mesmo papel que o React. O Hub usa React, e aprender os dois agora divide o teu tempo.
- **Kafka:** não é um framework. É um sistema de troca de mensagens para sistemas grandes, e nada no Hub usa.
- **Spring Boot:** é Java, uma linguagem inteira a mais. Entra no fim do Nível 6, porque a meta é empresa grande e muitas delas usam Java.

## Hábito semanal: 1 termo do Hub (10 min)

Quando aparecer uma palavra que tu não entendes, anota. Uma vez por semana, escolhe uma e escreve duas linhas: o que é, e onde aparece no Hub. Para começar: *migration*, *RLS*, *API*, *endpoint*, *JSON*, *schema*, *hook*, *soft delete*.

## Cuidado ao estudar pelo Hub

- **Para estudar, só lê.** Não rodes comandos do Hub sem saber o que eles fazem. O `npm run db:reset`, por exemplo, apaga o banco local.
- **O Hub cresce mais rápido do que tu aprendes.** Isso é esperado. O padrão que se repete em todos os módulos (rotas → serviço → repositório) importa mais do que a quantidade de código.
