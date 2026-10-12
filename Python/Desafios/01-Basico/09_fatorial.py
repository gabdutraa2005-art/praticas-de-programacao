"""
Desafio 09 - Fatorial (com loop E com recursao)
Nivel: Basico

Objetivo:
    Implemente o calculo do fatorial de duas formas diferentes:
    1. fatorial_loop(n): usando um for ou while.
    2. fatorial_recursivo(n): usando recursao (a funcao chama a si
       mesma ate o caso base n <= 1).

Exemplos:
    fatorial_loop(5)       -> 120
    fatorial_recursivo(5)  -> 120
    fatorial_loop(0)       -> 1
"""


def fatorial_loop(n):
    # TODO: implemente com loop
    pass


def fatorial_recursivo(n):
    # TODO: implemente com recursao
    # dica: caso base -> if n <= 1: return 1
    pass


if __name__ == "__main__":
    print(fatorial_loop(5))
    print(fatorial_recursivo(5))

    # assert fatorial_loop(5) == 120
    # assert fatorial_recursivo(5) == 120
    # assert fatorial_loop(0) == 1
