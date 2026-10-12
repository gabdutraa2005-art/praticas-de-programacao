"""
Desafio 05 - Arvore Binaria de Busca (BST)
Nivel: Avancado

Objetivo:
    Implemente uma Arvore Binaria de Busca com:
    - inserir(valor)
    - buscar(valor) -> True/False
    - percurso_em_ordem() -> lista com os valores em ordem crescente

Regra da BST:
    Para cada no, valores menores vao para a esquerda e valores
    maiores (ou iguais) vao para a direita.
"""


class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        # TODO: se a arvore estiver vazia, valor vira a raiz.
        # Caso contrario, desca recursivamente comparando valores
        # ate achar o lugar correto (menor -> esquerda, maior -> direita)
        pass

    def buscar(self, valor):
        # TODO: percorra a arvore comparando valor com cada no
        pass

    def percurso_em_ordem(self):
        # TODO: percurso "in-order": esquerda, no, direita
        # isso retorna os valores em ordem crescente
        resultado = []
        return resultado


if __name__ == "__main__":
    arvore = ArvoreBinariaBusca()
    for v in [5, 3, 8, 1, 4, 7, 9]:
        arvore.inserir(v)

    print(arvore.buscar(4))   # True
    print(arvore.buscar(6))   # False
    print(arvore.percurso_em_ordem())  # [1, 3, 4, 5, 7, 8, 9]
