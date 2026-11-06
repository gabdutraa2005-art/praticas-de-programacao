# fazer um jogo de pedra, papel e tesoura
from random import randint
from time import sleep
itens = ('Pedra', 'Pape', 'Tesoura')
computador = randint(0 ,2 )
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')
jogador = int(input('Qual é a sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('Computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))
if computador == 0: # o computador jogou PEDRA
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador Vence')
    elif jogador == 2:
        print('O computador Vence')
    else:
        print('Jogada invalida')
elif computador == 1:  # o computador jogou PAPEL
    if jogador == 0:
        print('O computador Vence')
    elif jogador == 1:
        print*('Empate')
    elif jogador == 2:
        print('O jogador vence')
    else:
        print('Jogada invalida')
elif computador == 2: # o computador jogou TESOURA
    if jogador == 0:
        print('O Jogador vence')
    elif jogador == 1:
        print('O computador Vence')
    elif jogador == 2:
        print('Empate')
    else:
        print('Jogada invalida')

# fiz com o guanabara, percebi que é so pensar mas e treinar mas
# pensar mas em bibliotecas em ex mas grande para ficar mas completos