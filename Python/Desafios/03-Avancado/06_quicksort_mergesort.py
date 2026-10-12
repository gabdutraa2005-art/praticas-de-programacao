"""
Desafio 06 - Quicksort e Mergesort
Nivel: Avancado

Objetivo:
    Implemente os dois algoritmos de ordenacao abaixo, sem usar
    sorted() ou list.sort():

    - quicksort(lista): escolhe um pivo, separa menores e maiores,
      ordena recursivamente cada lado e junta tudo.

    - mergesort(lista): divide a lista ao meio recursivamente ate
      sobrar 1 elemento, depois junta (merge) as metades ordenadas.

Exemplo:
    quicksort([5, 2, 9, 1, 5])   -> [1, 2, 5, 5, 9]
    mergesort([5, 2, 9, 1, 5])   -> [1, 2, 5, 5, 9]
"""


def quicksort(lista):
    # TODO: caso base: lista com 0 ou 1 elemento ja esta ordenada
    # escolha um pivo (ex: o do meio), separe menores/iguais/maiores
    # e retorne quicksort(menores) + iguais + quicksort(maiores)
    pass


def mergesort(lista):
    # TODO: caso base: lista com 0 ou 1 elemento ja esta ordenada
    # divida ao meio, chame mergesort recursivamente nas duas metades
    # e combine com uma funcao auxiliar merge(esquerda, direita)
    pass


def merge(esquerda, direita):
    # TODO: funcao auxiliar que junta duas listas ja ordenadas em
    # uma unica lista ordenada
    pass


if __name__ == "__main__":
    print(quicksort([5, 2, 9, 1, 5]))
    print(mergesort([5, 2, 9, 1, 5]))
