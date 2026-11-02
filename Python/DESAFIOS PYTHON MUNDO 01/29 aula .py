velocidade = float(input("Qual velocidade o seu carro estava?"))
print('Lendo...')
excesso = velocidade - 80
valor = excesso * 7
if excesso:
    print('Você foi multado! No valor de {}'.format(valor))
else:
    print ("Você não tem multa pendente, Parabéns!")