"""
Desafio 06 - Classe ContaBancaria (POO)
Nivel: Intermediario

Objetivo:
    Crie a classe ContaBancaria com:
    - atributos: titular, saldo (comeca em 0)
    - metodo depositar(valor): soma ao saldo (valor deve ser positivo)
    - metodo sacar(valor): subtrai do saldo, mas impede saque maior
      que o saldo disponivel (imprima uma mensagem de erro)
    - metodo extrato(): imprime titular e saldo atual

Exemplo de uso:
    conta = ContaBancaria("Joao")
    conta.depositar(100)
    conta.sacar(30)
    conta.extrato()  # Titular: Joao | Saldo: R$ 70.00
"""


class ContaBancaria:
    def __init__(self, titular):
        # TODO: inicialize titular e saldo
        pass

    def depositar(self, valor):
        # TODO: valide que valor > 0 e some ao saldo
        pass

    def sacar(self, valor):
        # TODO: valide saldo suficiente antes de subtrair
        pass

    def extrato(self):
        # TODO: imprima titular e saldo formatado com 2 casas decimais
        pass


if __name__ == "__main__":
    conta = ContaBancaria("Joao")
    conta.depositar(100)
    conta.sacar(30)
    conta.extrato()
    conta.sacar(1000)
