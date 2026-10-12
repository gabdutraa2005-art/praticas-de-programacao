"""
Desafio 02 - Contador de Palavras
Nivel: Intermediario

Objetivo:
    Escreva a funcao contar_palavras(texto) que retorna um dicionario
    com a quantidade de vezes que cada palavra aparece no texto.
    Ignore maiusculas/minusculas e pontuacao basica (. , ! ?).

Exemplo:
    contar_palavras("o gato e o cachorro")
        -> {"o": 2, "gato": 1, "e": 1, "cachorro": 1}

Dicas:
    - texto.lower().split() separa as palavras.
    - Use um dicionario para guardar as contagens.
"""


def contar_palavras(texto):
    # TODO: remova pontuacao, separe as palavras e conte cada uma
    pass


if __name__ == "__main__":
    resultado = contar_palavras("O gato e o cachorro. O gato dorme!")
    print(resultado)
