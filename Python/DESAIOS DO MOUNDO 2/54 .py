## faça um contador que vai pegar a data de nascimento de 7 pessoas e vai falar quantas atingiram a maior idade
from datetime import date
soma = 0
for c in range(1,8):
    nascimento = int(input('Digite a sua data de Nascimento:'))
    idade = date.today().year - nascimento
    if idade >=18:
        soma = soma + 1
print('{} são o numero de pessoas que são maior de idade'.format(soma))

#O código, linha por linha

#from datetime import date
#Traz a ferramenta date, que sabe a data de hoje. Sem ela, o programa não teria como saber o ano atual.


#soma = 0
#Cria o contador de maiores de idade. Começa em 0 porque, antes de perguntar qualquer pessoa, ninguém foi contado. Fica antes do for para não voltar a 0 a cada volta.


#for c in range(1, 8):
#Repete tudo o que está recuado embaixo 7 vezes, uma por pessoa. O c vale 1, 2… até 7, e só serve para contar as voltas.


 #   nascimento = int(input('Digite a sua data de Nascimento:'))
  #  idade = date.today().year - nascimento
#A cada volta, pergunta o ano de nascimento de uma pessoa e calcula a idade dela: o ano de hoje menos o ano em que ela nasceu.


 ##      soma = soma + 1
#Se essa pessoa tem 18 anos ou mais, o contador aumenta 1. Se não tem, nada acontece, e o for passa para a próxima pessoa.


#print('{} são o numero de pessoas que são maior de idade'.format(soma))
#Fica sem recuo, então só roda depois das 7 voltas, quando a contagem já terminou. Mostra o total.

#O que aconteceu no teste
#Volta	Ano	Idade	18 ou mais?	soma depois
#1	2000	26	sim	1
#2	2010	16	não	1
#3	1990	36	sim	2
#4	2015	11	não	2
#5	1980	46	sim	3
#6	2005	21	sim	4
#7	2012	14	não	4
#Revisão
#O que ficou bom: você juntou sozinho três peças de exercícios diferentes: o date do 39, o input dentro do for do 50 e o contador do 52.

#Uma coisa a melhorar: o nome soma não combina com o que a variável faz, porque ela conta pessoas, não soma valores. Um nome como maiores deixa a linha 8 legível como uma frase: "maiores = maiores + 1".