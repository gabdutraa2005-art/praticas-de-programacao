"""
Desafio 03 - Validador de CPF (formato)
Nivel: Intermediario

Objetivo:
    Escreva a funcao formato_valido(cpf) que verifica se uma string
    tem o FORMATO de um CPF: 11 digitos numericos, podendo vir com
    pontos e traco (ex: "123.456.789-09" ou "12345678909").

    Obs: este desafio valida apenas o FORMATO, nao os digitos
    verificadores reais do CPF (pode ser um desafio bonus!).

Exemplos:
    formato_valido("123.456.789-09") -> True
    formato_valido("12345678909")    -> True
    formato_valido("123.456.789")    -> False
    formato_valido("abc.def.ghi-jk") -> False
"""


def formato_valido(cpf):
    # TODO: remova pontos e tracos, depois verifique se sobraram
    # exatamente 11 caracteres e todos sao digitos (str.isdigit())
    pass


if __name__ == "__main__":
    print(formato_valido("123.456.789-09"))
    print(formato_valido("12345678909"))
    print(formato_valido("123.456.789"))
    print(formato_valido("abc.def.ghi-jk"))
