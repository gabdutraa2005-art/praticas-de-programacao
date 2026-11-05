# esse ex pede para eu refazer o 35, vou colar o codigo abaixo:
r1 = float(input("Qual é o tamanho da sua reta?"))
r2 = float(input("Qual é o tamamho da sua reta?"))
r3 = float(input("Qual é o tamanho da sua reta?"))
triangulo = r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2
# fizemos todo o tipo de variaveis que o usuario poderia fazer
if triangulo:
    print('Você vai conseguir formar um triangulo!')
else:
    print("Você não vai conseguir formar o triangulo")