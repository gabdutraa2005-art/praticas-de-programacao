"""
Desafio 08 - Busca Binaria
Nivel: Intermediario

Objetivo:
    Implemente busca_binaria(lista_ordenada, alvo) que retorna o
    INDICE do valor procurado, ou -1 se nao encontrar. A lista de
    entrada JA ESTA ORDENADA.

Exemplo:
    busca_binaria([1, 3, 5, 7, 9, 11], 7)  -> 3
    busca_binaria([1, 3, 5, 7, 9, 11], 4)  -> -1

Como funciona (resumo):
    Compare o alvo com o elemento do meio da lista.
    Se for igual, achou. Se o alvo for menor, busque na metade
    esquerda. Se for maior, busque na metade direita. Repita.
"""


def busca_binaria(lista_ordenada, alvo):
    # TODO: implemente com dois ponteiros (inicio e fim) ou recursao
    pass


if __name__ == "__main__":
    numeros = [1, 3, 5, 7, 9, 11]
    print(busca_binaria(numeros, 7))
    print(busca_binaria(numeros, 4))
