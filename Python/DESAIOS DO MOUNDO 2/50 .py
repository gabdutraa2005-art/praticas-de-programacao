## faz um programa que faça com que, leia seis numero inteiros e monstre a sema apenas daqueles que forem pares
## se o valor por impar desconsidere
soma = 0
for c in range(1, 7):
    n = int(input('Qual numero você quer?'))
    if n % 2 == 0:
        soma = soma + n
print('A soma foi de {}'.format(soma))