viagem = float(input("Qual Km deu a sua viagem?"))
print("Analisando..")
v1 = viagem * 0.50
v2 = viagem * 0.45
if viagem <=200:
    print("Você tera que pagar {}".format(v1))
else:
    print("Você tera que pagar {}".format(v2))