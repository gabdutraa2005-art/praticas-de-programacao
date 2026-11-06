# fazer um programa que leia o IMC do usario, com peso e altura
peso = float(input('Qual é o seu peso?'))
altura = float(input('Qual sua altura?'))
# conta do IMC calcular sua altura multiplicando por ela mesma e depois com o seu peso divida o resultado
# r1 aqui é somente um complemento para o calculo da imc
r1 = altura * altura
imc = peso / r1
if imc < 18.5:
    print('Abaixo do peso')
elif imc <=25:
    print('Peso ideal')
elif imc <=30:
    print('Sobrepeso')
elif imc <=40:
    print('Obesidade')
else:
    print('Obesidade morbida')
# claude usei a mesma base do ex 40 e 41, pulando as perguntas, pois o proprio python já vai pulando.
# <  não entra <= entra