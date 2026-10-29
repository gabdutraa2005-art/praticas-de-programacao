git status
git add -A
git commit -m "Descreva aqui o que você fez"
git push

O que cada um faz:

git status mostra o que mudou desde o último commit (arquivos novos, alterados ou apagados). É bom rodar antes para conferir.
git add -A separa todas essas mudanças para entrarem no próximo commit.
git commit -m "..." cria um "ponto de salvamento" no seu computador, com uma mensagem explicando a mudança. Por exemplo: "Adiciona exercícios da aula 09".
git push envia esses commits para o GitHub.
Dica: o git push só envia o que já virou commit. Se você esquecer o add e o commit, nada novo vai aparecer no GitHub.

Seu terminal está logado em duas contas do GitHub, gabdutraa2005-art e gabdutraa1406-cloud. A ativa é a gabdutraa2005-art, que é a dona desse repositório, então está tudo certo. Se um dia o push der erro de permissão, rode gh auth status para ver qual conta está ativa.