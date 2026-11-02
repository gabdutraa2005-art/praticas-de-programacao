# Desafio 33: mostrar o maior e o menor de tres numeros.
# Explicacao com tres criancas que mostram os numeros 5, 2 e 9.

# Guardando os numeros (input):
# cada numero vai para um potinho com nome: n1, n2 e n3.
n1 = int(input("Digite o primeiro numero:"))
n2=int(input("Digite outro numero:"))
n3 = int(input("Digite outro numero:"))

# Achando o menor:
# a caixa "menor" guarda so um numero por vez.
# 1. O 5 chega primeiro e entra na caixa.
# 2. O 2 pergunta: "Sou menor que o 5?". Sim, entao o 2 entra e o 5 sai.
# 3. O 9 pergunta: "Sou menor que o 2?". Nao, entao o 9 vai embora.
# A caixa fica com o 2.
menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

# Achando o maior:
# a caixa "maior" faz a mesma brincadeira, perguntando "Sou maior?".
# 1. O 5 entra na caixa.
# 2. O 2 pergunta: "Sou maior que o 5?". Nao, entao ele vai embora.
# 3. O 9 pergunta: "Sou maior que o 5?". Sim, entao o 9 entra e o 5 sai.
# A caixa fica com o 9.
maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
    # Mostrando o resultado (print e .format):
    # a frase e um desenho com dois espacinhos vazios, os {}.
    # O .format(maior, menor) cola os numeros neles, na ordem:
    # o maior no primeiro espacinho e o menor no segundo.
    # Recuo: o que tem recuo so acontece se a resposta do if for sim.
    # Sem recuo, acontece sempre.
    print("O seu numero maior foi de {} e o menor foi de {}".format(maior,menor))


