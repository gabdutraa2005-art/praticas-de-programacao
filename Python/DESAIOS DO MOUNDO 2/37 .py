numero = int(input("Qual numero você deseja fazer a conversão?"))
print('1-Para binario')
print('2-Para octal')
print('3-Para Hexadecimal')
opcao = int(input("Escolha a sua opção:"))
if opcao == 1:
    print(bin(numero))
elif opcao == 2:
    print(oct(numero))
elif opcao == 3:
    print(hex(numero))