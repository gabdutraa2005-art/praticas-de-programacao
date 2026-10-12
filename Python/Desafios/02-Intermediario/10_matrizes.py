"""
Desafio 10 - Operacoes com Matrizes
Nivel: Intermediario

Objetivo:
    Usando listas de listas (ex: [[1, 2], [3, 4]]), implemente:
    - somar_matrizes(m1, m2): soma elemento a elemento
    - transposta(m): troca linhas por colunas
    - multiplicar_matrizes(m1, m2): multiplicacao matricial classica

Exemplo:
    m1 = [[1, 2], [3, 4]]
    m2 = [[5, 6], [7, 8]]
    somar_matrizes(m1, m2)  -> [[6, 8], [10, 12]]
    transposta(m1)          -> [[1, 3], [2, 4]]
"""


def somar_matrizes(m1, m2):
    # TODO: percorra linha a linha, coluna a coluna, somando
    pass


def transposta(m):
    # TODO: a linha i, coluna j vira linha j, coluna i
    pass


def multiplicar_matrizes(m1, m2):
    # TODO: para cada linha de m1 e coluna de m2, some os produtos
    pass


if __name__ == "__main__":
    m1 = [[1, 2], [3, 4]]
    m2 = [[5, 6], [7, 8]]
    print(somar_matrizes(m1, m2))
    print(transposta(m1))
    print(multiplicar_matrizes(m1, m2))
