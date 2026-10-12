"""
Desafio 10 - Projeto Final: Sistema de Biblioteca
Nivel: Avancado

Objetivo:
    Junte TUDO que voce praticou (POO, arquivos JSON, excecoes,
    estruturas de dados) para construir um sistema de biblioteca
    simples via terminal.

Requisitos:
    1. Classe Livro: titulo, autor, ano, disponivel (bool, comeca True)
    2. Classe Biblioteca:
       - acervo: lista de objetos Livro
       - adicionar_livro(livro)
       - emprestar_livro(titulo): marca disponivel=False (se existir
         e estiver disponivel; senao avisa o usuario)
       - devolver_livro(titulo): marca disponivel=True
       - listar_disponiveis(): mostra so os livros disponiveis
       - salvar_em_json(caminho): persiste o acervo em arquivo
       - carregar_de_json(caminho): recupera o acervo salvo
    3. Menu de terminal que usa todas as funcionalidades acima e
       carrega/salva automaticamente ao iniciar/sair.

Esse e o desafio mais completo da trilha: pegue seu tempo, quebre
em pequenas partes e va testando cada metodo isoladamente antes de
montar o menu completo.
"""
import json
import os


class Livro:
    def __init__(self, titulo, autor, ano, disponivel=True):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = disponivel

    def to_dict(self):
        # TODO: retorne um dicionario representando o livro
        # (util para salvar em json)
        pass

    @staticmethod
    def from_dict(dados):
        # TODO: crie e retorne um objeto Livro a partir de um dict
        pass


class Biblioteca:
    def __init__(self):
        self.acervo = []

    def adicionar_livro(self, livro):
        # TODO
        pass

    def emprestar_livro(self, titulo):
        # TODO
        pass

    def devolver_livro(self, titulo):
        # TODO
        pass

    def listar_disponiveis(self):
        # TODO
        pass

    def salvar_em_json(self, caminho="biblioteca.json"):
        # TODO: converta cada livro com to_dict() e salve a lista
        pass

    def carregar_de_json(self, caminho="biblioteca.json"):
        # TODO: se o arquivo existir, carregue e recrie os objetos
        # Livro com Livro.from_dict(...)
        pass


def menu():
    biblioteca = Biblioteca()
    biblioteca.carregar_de_json()

    while True:
        print("\n1-Adicionar 2-Emprestar 3-Devolver 4-Listar 5-Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            # TODO: peca titulo, autor, ano e crie/adicione um Livro
            pass
        elif opcao == "2":
            # TODO: peca o titulo e chame emprestar_livro
            pass
        elif opcao == "3":
            # TODO: peca o titulo e chame devolver_livro
            pass
        elif opcao == "4":
            biblioteca.listar_disponiveis()
        elif opcao == "5":
            biblioteca.salvar_em_json()
            print("Ate mais!")
            break


if __name__ == "__main__":
    menu()
