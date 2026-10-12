"""
Desafio 01 - Lista de Compras (menu no terminal)
Nivel: Intermediario

Objetivo:
    Crie um programa com menu em loop que permita:
    1. Adicionar item
    2. Remover item
    3. Listar itens
    4. Sair

    Use uma lista em memoria para guardar os itens.

Exemplo de interacao:
    1 - Adicionar | 2 - Remover | 3 - Listar | 4 - Sair
    Escolha: 1
    Item: Arroz
    Item adicionado!
"""


def menu():
    itens = []
    while True:
        print("\n1 - Adicionar | 2 - Remover | 3 - Listar | 4 - Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            # TODO: peca o nome do item e adicione na lista
            pass
        elif opcao == "2":
            # TODO: peca o nome do item e remova da lista (cuidado se nao existir)
            pass
        elif opcao == "3":
            # TODO: imprima todos os itens (ou avise que a lista esta vazia)
            pass
        elif opcao == "4":
            print("Ate mais!")
            break
        else:
            print("Opcao invalida.")


if __name__ == "__main__":
    menu()
