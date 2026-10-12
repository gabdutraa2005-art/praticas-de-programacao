"""
Desafio 03 - Torres de Hanoi
Nivel: Avancado

Objetivo:
    Implemente a solucao recursiva classica do problema das Torres
    de Hanoi. A funcao deve imprimir cada movimento feito.

Assinatura:
    hanoi(n, origem, auxiliar, destino)

Exemplo de uso:
    hanoi(3, "A", "B", "C")
    # Mova disco 1 de A para C
    # Mova disco 2 de A para B
    # Mova disco 1 de C para B
    # ...

Como pensar:
    Para mover n discos de origem para destino usando auxiliar:
    1. Mova n-1 discos de origem para auxiliar (usando destino de apoio)
    2. Mova o disco n de origem para destino
    3. Mova n-1 discos de auxiliar para destino (usando origem de apoio)
    Caso base: n == 0, nao faz nada.
"""


def hanoi(n, origem, auxiliar, destino):
    # TODO: implemente a recursao descrita acima
    pass


if __name__ == "__main__":
    hanoi(3, "A", "B", "C")
