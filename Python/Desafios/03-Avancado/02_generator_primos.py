"""
Desafio 02 - Generator de Numeros Primos (infinito)
Nivel: Avancado

Objetivo:
    Escreva o generator gerador_primos() que produz numeros primos
    um a um, infinitamente (usando yield), sem gerar uma lista
    gigante na memoria.

Exemplo de uso:
    gen = gerador_primos()
    for _ in range(5):
        print(next(gen))
    # 2, 3, 5, 7, 11

Dicas:
    - Um generator usa "yield" em vez de "return".
    - Para cada candidato, teste se e divisivel por algum primo
      ja encontrado antes de considera-lo primo.
"""


def eh_primo(n, primos_encontrados):
    # TODO: retorne True se n nao for divisivel por nenhum numero
    # da lista primos_encontrados (ate a raiz quadrada de n)
    pass


def gerador_primos():
    # TODO: use um loop infinito (while True) com yield para
    # produzir primos um a um, guardando os ja encontrados
    pass


if __name__ == "__main__":
    gen = gerador_primos()
    for _ in range(10):
        print(next(gen))
