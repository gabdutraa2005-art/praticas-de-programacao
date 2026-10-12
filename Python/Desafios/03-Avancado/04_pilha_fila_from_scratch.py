"""
Desafio 04 - Pilha e Fila do Zero
Nivel: Avancado

Objetivo:
    Implemente as classes Pilha (LIFO) e Fila (FIFO) usando apenas
    listas internamente, sem usar collections.deque.

Classe Pilha:
    - empilhar(item)
    - desempilhar() -> remove e retorna o topo (ou None se vazia)
    - topo() -> olha o topo sem remover
    - esta_vazia() -> bool

Classe Fila:
    - enfileirar(item)
    - desenfileirar() -> remove e retorna o primeiro (ou None se vazia)
    - esta_vazia() -> bool
"""


class Pilha:
    def __init__(self):
        self._itens = []

    def empilhar(self, item):
        # TODO
        pass

    def desempilhar(self):
        # TODO
        pass

    def topo(self):
        # TODO
        pass

    def esta_vazia(self):
        # TODO
        pass


class Fila:
    def __init__(self):
        self._itens = []

    def enfileirar(self, item):
        # TODO
        pass

    def desenfileirar(self):
        # TODO
        pass

    def esta_vazia(self):
        # TODO
        pass


if __name__ == "__main__":
    pilha = Pilha()
    pilha.empilhar(1)
    pilha.empilhar(2)
    print(pilha.desempilhar())  # 2

    fila = Fila()
    fila.enfileirar(1)
    fila.enfileirar(2)
    print(fila.desenfileirar())  # 1
