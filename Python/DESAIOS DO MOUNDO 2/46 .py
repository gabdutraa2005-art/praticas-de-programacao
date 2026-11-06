# fazer um programa que monstre os fogos estourando, com a contagem regrassiva de 10 ate 0 com pausa de 1 segundo
from time import sleep
for c in range(10, -1, -1): # vai de 10 a 0.
    print(c)
    sleep(1)
print('Feliz Ano Novo! 🎆🎇')