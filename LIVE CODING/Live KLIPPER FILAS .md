Live coding da Fernanda klliper com vite-react e TS

Projeto com objetivo- Backend em Node.js, Vai receber evento numa fila e coloca no reedis, que esta na AWS, esse proprio backend vai consumir esse evento da fila.

Oque são filas?- São serapações no backend, ex: uma parte para enviar email outra produtos e assim por diante. Mas são serviços independetes, ou seja, caiu uma das filas a outra continua.

Nessa aplicação vai ser trabalhado em micro serviços, ou seja, ela vai fazer varios front para falar com as FILAS para essa aplicação que esta hospedada na AWS.

Quando ela vai puxar o vite na api ela usa- npm create vite@latest

Ela vai usar o chakra com biblioca de desing, ela também deu uma tima bacana para desenvolvimento que é escolhor uma biblioteca que não pese tanto.

Palavras que não entendi:
Tipagem

  # claude escreve os resultados aqui-

**Tipagem**: dizer qual tipo de dado uma variável aceita (texto, número, verdadeiro/falso).
- Você já conhece os tipos do Python: `int`, `float`, `str`, `bool`.
- No TypeScript você escreve o tipo: `let idade: number = 20`.
- Se tentar `idade = "vinte"`, o editor avisa o erro **antes** de rodar.
- É o principal motivo de usar TS em vez de JS puro.

Vou deixar um comentario para eu ver no futuro, quando eu tiver mas avançado aqui:
Estou percebendo que, mesmo ela sendo um Junior, tem um abismo de diferença no estagio que estou, ela já denomina bem variavel, fluente em JS e outras frame works, em desenvolvimento de software e na propria linguagem não tem comparação comigo. 
Sempre olha a Wiki para relembrar, na epoca dela não tinha tantas IA mas mesmo assim o dev sempre tem que olhar wiki.
Como ela começo com desenvolvimento, escolheu o framework, foi de vite + react + TS, começou com o desing, mexeu no HTML e CSS, e depois foi para o prosseco de chamadas, isso é relativo a dev e estilo de trabalho, aplicação e enfim.


 # claude escreve os oque você achou sobre o meu resumo aqui-

**O que está certo**
- Backend em Node.js, Vite + React + TS no front, Chakra como biblioteca de componentes.
- A dica de escolher bibliotecas leves é ótima.
- A observação sobre o jeito dela trabalhar (escolher a stack, depois visual, depois as chamadas) é muito boa.

**Ajustes**
- O nome é **Fernanda Kipper**.
- **Redis**: um banco de dados muito rápido que guarda tudo na memória. Muito usado como fila e como cache.
- **Fila** é uma lista de tarefas esperando para serem processadas, em ordem: a primeira que entra é a primeira que sai.
  - Um serviço coloca a tarefa na fila (ex.: "enviar email para fulano").
  - Outro serviço pega a tarefa e executa, no seu próprio ritmo.
  - Se o serviço que executa cair, as tarefas ficam esperando na fila e não se perdem.
- O que você descreveu na linha das filas (partes separadas para email, produtos etc.) são os **microsserviços**. As filas são o jeito de eles conversarem sem depender um do outro.
- O front provavelmente não fala direto com a fila: ele chama o backend (a API), e o backend coloca na fila. É a mesma ideia do React com o PostgreSQL.
- `npm create vite@latest` cria um **projeto novo de front-end** (React + TS), não a API.

**Sobre a sua reflexão**
- A diferença que você sentiu é normal: ela tem anos de prática a mais. Compare você com você de um mês atrás, não com ela.
- Consultar a documentação o tempo todo é normal em qualquer nível. Ninguém decora tudo.
- Perceber o *processo* dela, e não só o código, mostra que você está assistindo do jeito certo.