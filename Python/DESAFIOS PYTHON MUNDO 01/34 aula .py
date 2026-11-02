salario = float(input("Qual seu salario?"))
maior = salario * 0.10
menor = salario * 0.15
if salario >=1250:
    print("Seu aumento foi de {}".format(maior))
else:
    print("Seu aumento foi de {}".format(menor))  

