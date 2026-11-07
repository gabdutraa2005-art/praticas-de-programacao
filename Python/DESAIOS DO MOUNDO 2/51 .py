## desenvolver um programa que desenvolvar uma uma progressão aritmetica, ele vai ler uma PA e vai dizer ce o primeiro termo e a razão final monstra os 10 primeiros termos dessa progressão

a1 = int(input('Qual é o seu primeiro termo?'))
razao = int(input('Qual é a sua razão?'))
decimo = a1 + 9 * razao
for c in range(a1, decimo , razao):
    print(c)


##O código, de forma geral

##Linhas 3 e 4, as entradas:
##a1 = int(input('Qual é o seu primeiro termo?'))
##razao = int(input('Qual é a sua razão?'))
##O programa pergunta os dois únicos valores que definem uma PA: onde ela começa e de quanto em quanto ela anda.

##Linha 5, onde a PA termina:
##decimo = a1 + 9 * razao
##Calcula o décimo termo antes de mostrar qualquer coisa. Ele é o primeiro termo mais 9 razões, porque cada termo tem uma razão a menos que a sua posição.

##Linhas 6 e 7, mostrar os termos:
##for c in range(a1, decimo, razao):
 ##   print(c)
##Aqui o range faz quase todo o trabalho, com as três partes que você já conhece:

##Parte do range	Valor	Significado
##início	a1	a PA começa no primeiro termo
##fim	decimo (+ razão)	a PA vai até o décimo termo
##passo	razao	a PA anda de razão em razão
##A cada volta, o c vale um termo da PA, e o print(c) mostra esse termo.

##A ideia principal: uma PA é um range. Os pares do 47 eram uma PA com início 2 e razão 2. A diferença é que aqui os três valores vêm da pessoa, em vez de estarem fixos no código.