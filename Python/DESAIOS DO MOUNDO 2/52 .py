## faça um programa que leia um numero inteiro e diga se ele é ou não um numero primo
# primo somente 1 e por ele mesmo
soma = 0
numero = int(input('Qual seu numero escolhido?'))
for c in range(1,numero + 1):
    if numero % c == 0:
        soma = soma + 1
    if numero % c == 0:
        print('Seu numero é primo')
    else:
        print('Não tem primo')


#Linhas 3 a 7: estão certas

#soma = 0
#Cria o contador de divisores. Começa em 0 porque, antes de testar qualquer número, nenhum divisor foi encontrado.


##numero = int(input('Qual seu numero escolhido?'))
#Pergunta o número que vai ser testado e transforma em inteiro.


#for c in range(1, numero + 1):
#Faz o c passar por todos os candidatos a divisor, de 1 até o próprio número. O + 1 existe porque o fim do range nunca é incluído, e o próprio número precisa ser testado.


#    if numero % c == 0:
##        soma = soma + 1
#A cada volta, pergunta: "o número dividido por c sobra zero?". Se sim, o c é um divisor, e o contador aumenta 1. No fim do for, a soma guarda quantos divisores o número tem: 2 para o 7, e 4 para o 8.

#Linhas 8 a 11: é aqui que está o erro

#    if numero % c == 0:
#        print('Seu numero é primo')
#    else:
#        print('Não tem primo')
#O que esse bloco faz hoje:

##Ele está recuado, dentro do for: por isso roda a cada volta, e não uma vez no final.
##Ele repete a pergunta da linha 6: "divide por c?". Então ele diz "é primo" toda vez que acha um divisor. Isso não tem relação com o número ser primo.
#O que esse bloco deveria fazer: rodar uma vez, depois do for, e olhar para o contador, perguntando se ele deu exatamente 2.

#Então são duas mudanças: o recuo (sair de dentro do for) e a pergunta (olhar a variável que contou os divisores). Faça as duas e me peça para rodar com 7, 8 e 2.