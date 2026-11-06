# realizar descontos sobre pagamento
preço = float(input('Qual é valor do item?'))
print('1 - Cheque/Dinheiro')
print('2 - Avista no Cartão')
print('3 - 2x no cartão')
print('4 - 3x ou mais no cartão')
escolha = int(input('Escolha sua opção:'))
cheque = preço * 0.10
cheque2 = preço - cheque
cartao = preço * 0.05
cartao2 = preço - cartao
parcelado = preço * 0.20
parcelado2 = preço + parcelado
if escolha == 1:
    print('O valor do seu item ficara {}'.format(cheque2))
elif escolha == 2:
    print('O valor do seu item ficara {}'.format(cartao2))
elif escolha == 3:
    print ('O valor do seu item ficara {}'.format(preço))
elif escolha == 4:
    print('O valor do seu item ficara {}'.format(parcelado2))
# usei semelhante o ex 37