"""
Desafio 09 - Gerenciador de Tarefas (To-Do CLI com JSON)
Nivel: Intermediario

Objetivo:
    Junte os conceitos de menu, listas de dicionarios e arquivos
    JSON para criar um gerenciador de tarefas persistente.

    Cada tarefa e um dicionario com chaves "descricao" e "feita".

Funcionalidades do menu:
    1. Adicionar tarefa
    2. Marcar tarefa como feita (pelo indice)
    3. Listar tarefas (mostrando [X] feita ou [ ] pendente)
    4. Sair (salvando no arquivo tarefas.json)

Dica:
    - Reaproveite a logica de carregar/salvar json do desafio 04.
"""
import json
import os

ARQUIVO = "tarefas.json"


def carregar_tarefas():
    # TODO: leia o arquivo json ou retorne lista vazia
    pass


def salvar_tarefas(tarefas):
    # TODO: grave a lista de tarefas no arquivo
    pass


def menu():
    tarefas = carregar_tarefas()
    while True:
        print("\n1-Adicionar 2-Concluir 3-Listar 4-Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            # TODO: adicione um dicionario novo na lista de tarefas
            pass
        elif opcao == "2":
            # TODO: peca o indice e marque "feita" como True
            pass
        elif opcao == "3":
            # TODO: percorra e imprima com [X] ou [ ]
            pass
        elif opcao == "4":
            salvar_tarefas(tarefas)
            break


if __name__ == "__main__":
    menu()
