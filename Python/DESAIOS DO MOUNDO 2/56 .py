## vou ter que desenvolver um programa que vai ler o nome, idade e sexo de 4 pessoas, no final do programa monstre:
# a media de idade do grupo
# Qual é o nome do homem mas velho 
# quantas mulheres tem menos de 20 anos
soma = 0
mediaidade = 0 
maioridadehome = 0
nomevelho = ''
totmulher20 = 0
for p in range(1,5):
    print('---- {}ª PESSOA 0----'.format(p))
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma += idade
    if p == 1 and sexo in 'Mm':
        maioridadehome = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehome:
        maioridadehome = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = soma / 4
print('A media do grupo é de {}'.format(mediaidade))
print('O homem mas velho tem {} anos e se chama {}'.format(maioridadehome, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))