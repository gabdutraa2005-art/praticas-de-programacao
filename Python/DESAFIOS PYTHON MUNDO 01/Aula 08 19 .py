import random
n1 = input('Digite um nome:')
n2 = input('Digite outro nome:')
n3 = input('Digite mais um nome:')
n4 = input('Digite o último nome:')
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi o {}'.format(escolhido))