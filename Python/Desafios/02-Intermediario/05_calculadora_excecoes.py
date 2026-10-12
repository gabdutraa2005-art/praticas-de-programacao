"""
Desafio 05 - Calculadora com Tratamento de Excecoes
Nivel: Intermediario

Objetivo:
    Crie uma calculadora de terminal (soma, subtracao, multiplicacao,
    divisao) que NAO QUEBRA quando o usuario:
    - digita uma letra no lugar de um numero (ValueError)
    - tenta dividir por zero (ZeroDivisionError)
    - escolhe uma operacao invalida

    Use try/except para tratar cada caso com uma mensagem amigavel.

Exemplo de interacao:
    Primeiro numero: 10
    Segundo numero: 0
    Operacao (+ - * /): /
    Erro: nao e possivel dividir por zero.
"""


def calcular(a, b, operacao):
    # TODO: implemente as 4 operacoes, lancando ZeroDivisionError
    # naturalmente ao dividir por zero (o Python ja faz isso sozinho)
    pass


def main():
    try:
        a = float(input("Primeiro numero: "))
        b = float(input("Segundo numero: "))
        operacao = input("Operacao (+ - * /): ")
        resultado = calcular(a, b, operacao)
        print("Resultado:", resultado)
    except ValueError:
        print("Erro: digite apenas numeros validos.")
    except ZeroDivisionError:
        print("Erro: nao e possivel dividir por zero.")
    # TODO: trate tambem o caso de operacao invalida (dica: dentro de
    # calcular, use raise ValueError("operacao invalida") e capture aqui)


if __name__ == "__main__":
    main()
