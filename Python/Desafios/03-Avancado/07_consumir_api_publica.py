"""
Desafio 07 - Consumir uma API Publica
Nivel: Avancado

Objetivo:
    Use a biblioteca "requests" para consumir uma API publica
    gratuita e exibir os dados formatados no terminal.

    Sugestao de API (nao precisa de chave/autenticacao):
    https://viacep.com.br/ws/{cep}/json/  (consulta de CEP no Brasil)

Preparacao:
    pip install requests

Objetivo do codigo:
    - Peca um CEP ao usuario (ex: 01310930)
    - Faca a requisicao GET para a API
    - Trate o caso de CEP invalido ou erro de conexao
    - Imprima rua, bairro, cidade e estado

Dicas:
    - response = requests.get(url)
    - dados = response.json()
    - Use try/except requests.exceptions.RequestException para
      capturar problemas de rede.
"""
import requests


def buscar_endereco(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    # TODO: faca a requisicao, trate erros e retorne o dicionario
    # com os dados do endereco (ou None se o CEP for invalido)
    pass


if __name__ == "__main__":
    cep = input("Digite um CEP (somente numeros): ")
    endereco = buscar_endereco(cep)
    if endereco:
        print(endereco)
    else:
        print("CEP nao encontrado ou erro na consulta.")
