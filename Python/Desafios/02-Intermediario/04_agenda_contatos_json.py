"""
Desafio 04 - Agenda de Contatos com Persistencia em JSON
Nivel: Intermediario

Objetivo:
    Crie uma agenda de contatos (nome + telefone) que SALVA os dados
    em um arquivo "contatos.json" para nao perder as informacoes ao
    fechar o programa.

Funcoes a implementar:
    - carregar_contatos(): le o arquivo json e retorna um dict (ou {}
      se o arquivo nao existir ainda).
    - salvar_contatos(contatos): grava o dict no arquivo json.
    - adicionar_contato(contatos, nome, telefone): atualiza o dict.

Dicas:
    - Use "import json" e "import os".
    - Use os.path.exists("contatos.json") para checar se o arquivo existe.
    - json.dump(dados, arquivo, indent=4) escreve bonito e legivel.
"""
import json
import os

ARQUIVO = "contatos.json"


def carregar_contatos():
    # TODO: se o arquivo existir, leia e retorne o conteudo (json.load)
    # caso contrario, retorne um dicionario vazio
    pass


def salvar_contatos(contatos):
    # TODO: escreva o dicionario no arquivo em formato json
    pass


def adicionar_contato(contatos, nome, telefone):
    # TODO: adicione o par nome/telefone no dicionario
    pass


if __name__ == "__main__":
    contatos = carregar_contatos()
    adicionar_contato(contatos, "Maria", "11999990000")
    salvar_contatos(contatos)
    print(carregar_contatos())
