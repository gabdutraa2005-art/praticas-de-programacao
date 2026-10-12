"""
Desafio 02 - Par ou Impar
Nivel: Basico

Objetivo:
    Escreva a funcao eh_par(numero) que retorna True se o numero for
    par e False se for impar.

Exemplos:
    eh_par(4)  -> True
    eh_par(7)  -> False
    eh_par(0)  -> True
"""


def eh_par(numero):
    # TODO: implemente a logica usando o operador %
    pass


if __name__ == "__main__":
    for n in [4, 7, 0, -3, 10]:
        print(n, "->", eh_par(n))

    # Testes rapidos (descomente para validar sua solucao)
    # assert eh_par(4) is True
    # assert eh_par(7) is False
    # assert eh_par(0) is True
    # print("Todos os testes passaram!")
