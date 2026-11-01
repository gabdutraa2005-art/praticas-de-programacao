frase = str(input("Digite uma frase: ")) .upper()
print("A letra A aparece {} vezes na frase.".format(frase.lower().count("a")))
print("A primeira letra A aparece na posição {}.".format(frase.lower().find("a") + 1))
print("A última letra A aparece na posição {}.".format(frase.lower().rfind("a") + 1))

# o strip vai deixar o programa sem espaçoes o .upper vai deixar o maisculo dando certo