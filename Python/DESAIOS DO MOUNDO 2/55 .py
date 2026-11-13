## preciso fazer um programa que leia o peso de cinco pessoas, quando ele preciso dizer qual foi o peso maior e menor
for c in range(0,5): ## Começar no 0 é o que permite o if c == 0 reconhecer a primeira volta.
    peso = float(input('Qual é o seu peso?'))
    if c == 0: # não é a pessoa que vale 0, é o c que vale 0 na primeira volta. Algo como "na primeira volta (c vale 0), o peso entra direto nos dois papéis, porque ainda não tem com quem comparar".
        menor = peso   
        maior = peso
    else: # Cada novo peso vai ser substituído" não é verdade: o papel só é trocado quando o peso bate o recorde. Se não bater, o papel continua igual, como no 60 kg do jogo. Ajuste para dizer que, da segunda pessoa em diante, cada peso é comparado com os papéis.
        if peso > maior:# ce o peso for maior, o do papel vai ser trocado
            maior = peso
        if peso < menor:# ce o peso for menor, o do papel vai ser trocado
            menor = peso
print("Esse é o maior{}".format(maior))# ficaram fora do for, para indicar ele não precisa de mas pergunta, aqui já e a resposta
print('Esse é o menor{}'.format(menor))