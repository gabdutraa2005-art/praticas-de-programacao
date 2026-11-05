# programa que calcula a média do aluno
n1 = float(input("Qual sua nota?"))
n2 = float(input('Qual sua nota?'))
n3 = float(input('Qual sua nota?'))
# duas variaveis, uma para fazer a multiplicação e depois outra para realizar a média, poderia ter feito mas simples
vezes = n1 + n2 + n3
media = vezes / 3
if media < 5.0:
    print('Reprovado')
## idade >= 13: a primeira pergunta completa. and: liga as duas perguntas, e as duas têm que dar True. idade <= 17: a segunda pergunta completa.
elif media < 7.0:
    print('Recuperação')
else:
    print('Aprovado')
#O < exclui o número, então ele vai junto do número onde a próxima faixa começa (o 7).
#O <= inclui o número.
# Num "entre", cada lado do and precisa de uma comparação completa, com variável, sinal e valor.