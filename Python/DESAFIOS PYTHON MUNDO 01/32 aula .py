ano = int(input("Qual ano que estamos?"))
d1 = ano % 4
d2 = ano % 400
d3 = ano % 100
if (d1 == 0 and d2 !=0) or d3 ==0:
    print("Seu ano é bissexto!")
else:
    print("Seu ano não é bissexto!")