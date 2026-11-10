## crie um programa que identique se a frase que ele colocou é um palidromo
## palidromo a frase tem o mesmo significado mesmo de trás para frente

frase = input('Qual é a sua frase?') .upper() 
frase = frase.replace(' ','') ## o ' ' ele vai procurar dentro de um espaço e o '' vai achar algo nada
inverso = frase[::-1]
if frase == inverso:
    print('Sua Frase é um Polidromo Parabens!!')
    print('{}'.format(frase))
else:
    print('Sua frase não é um polidromo')

#Limpar: o .upper() iguala as letras, e o .replace(' ', '') tira os espaços.
##Inverter: o fatiamento [::-1], com o mesmo passo negativo da contagem regressiva.
#Comparar: o if frase == inverso, uma comparação completa, com as duas variáveis e o sinal.