"""
Desafio 08 - Testes Unitarios com unittest
Nivel: Avancado

Objetivo:
    Pratique testes automatizados. Abaixo ha uma funcao simples
    ja pronta (eh_primo). Sua tarefa e escrever a classe de testes
    TestEhPrimo cobrindo varios casos:
    - numeros primos conhecidos (2, 3, 5, 7, 11, 13)
    - numeros nao primos (1, 4, 6, 8, 9, 10)
    - casos extremos (0, numeros negativos)

Como rodar os testes:
    python 08_testes_unitarios.py

Dica:
    - Use self.assertTrue(...) e self.assertFalse(...)
    - Cada metodo de teste deve comecar com "test_"
"""
import unittest


def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


class TestEhPrimo(unittest.TestCase):
    def test_numeros_primos(self):
        # TODO: teste que 2, 3, 5, 7, 11, 13 sao primos
        pass

    def test_numeros_nao_primos(self):
        # TODO: teste que 1, 4, 6, 8, 9, 10 nao sao primos
        pass

    def test_casos_extremos(self):
        # TODO: teste 0 e numeros negativos (nao devem ser primos)
        pass


if __name__ == "__main__":
    unittest.main()
