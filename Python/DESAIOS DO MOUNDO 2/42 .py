# esse ex pede para eu refazer o 35, vou colar o codigo abaixo:
r1 = int(input("Qual é o tamanho da sua reta?"))
r2 = int(input("Qual é o tamamho da sua reta?"))
r3 = int(input("Qual é o tamanho da sua reta?"))
triangulo = r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2
equi = r1 == r2 == r3
iso = r1 == r2 or r3 == r2 or r1 == r3
if triangulo:
    print('Você vai conseguir formar um triangulo!')
# um if dentro de outro só é perguntado quando o de fora deu True. Por isso a pergunta de dentro tem que ser diferente da de fora.
    if equi:
        print('Você tem um tringulo Equilatero!')
    elif iso:
            print('Você tem um triangulo Isósceles')
    else:
            print('Você tem um escaleno')
# Perceba a piramide que é formado, tudo dentro de uma unica função
else:
    print("Você não vai conseguir formar o triangulo")
