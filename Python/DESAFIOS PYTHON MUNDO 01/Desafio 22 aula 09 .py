nome = str(input("Insira o seu nome: ")).strip()
print("Analisando o seu nome...")
print("Seu nome em maisculás é {}".format(nome.upper()))
print("Seu nome em minusculos é {}".format(nome.lower()))
print("Seu nome ao todo tem {}".format(len(nome)- nome.count ("")))
print("Seu nome tem {} letras".format(nome.find(" ")))


