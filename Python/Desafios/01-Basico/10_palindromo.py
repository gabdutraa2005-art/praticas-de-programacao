"""
Desafio 10 - Verificar Palindromo
Nivel: Basico

Objetivo:
    Escreva a funcao eh_palindromo(texto) que retorna True se o
    texto for igual lido de tras para frente, ignorando espacos e
    maiusculas/minusculas.

Exemplos:
    eh_palindromo("arara")          -> True
    eh_palindromo("A sacada da casa") -> True
    eh_palindromo("python")         -> False

Dica:
    - Remova espacos com texto.replace(" ", "") e normalize com
      texto.lower() antes de comparar.
"""


def eh_palindromo(texto):
    # TODO: normalize o texto e compare com sua versao invertida
    pass


if __name__ == "__main__":
    print(eh_palindromo("arara"))
    print(eh_palindromo("A sacada da casa"))
    print(eh_palindromo("python"))
