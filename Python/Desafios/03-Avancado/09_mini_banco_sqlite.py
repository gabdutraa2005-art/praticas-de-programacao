"""
Desafio 09 - Mini Banco de Dados com SQLite
Nivel: Avancado

Objetivo:
    Use o modulo "sqlite3" (ja vem com o Python, nao precisa instalar
    nada) para criar um CRUD simples de usuarios.

Funcoes a implementar:
    - criar_tabela(conexao): cria a tabela "usuarios" (id, nome, email)
      se ela ainda nao existir.
    - adicionar_usuario(conexao, nome, email): insere um registro.
    - listar_usuarios(conexao): retorna todos os registros.
    - remover_usuario(conexao, id_usuario): apaga pelo id.

Dicas:
    - import sqlite3
    - conexao = sqlite3.connect("banco.db")
    - cursor = conexao.cursor()
    - cursor.execute("CREATE TABLE IF NOT EXISTS ...")
    - Nao esqueca de conexao.commit() apos INSERT/DELETE.
"""
import sqlite3


def criar_tabela(conexao):
    # TODO: CREATE TABLE IF NOT EXISTS usuarios (
    #   id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT)
    pass


def adicionar_usuario(conexao, nome, email):
    # TODO: INSERT INTO usuarios (nome, email) VALUES (?, ?)
    pass


def listar_usuarios(conexao):
    # TODO: SELECT * FROM usuarios, retorne cursor.fetchall()
    pass


def remover_usuario(conexao, id_usuario):
    # TODO: DELETE FROM usuarios WHERE id = ?
    pass


if __name__ == "__main__":
    conexao = sqlite3.connect("banco.db")
    criar_tabela(conexao)
    adicionar_usuario(conexao, "Ana", "ana@email.com")
    print(listar_usuarios(conexao))
    conexao.close()
