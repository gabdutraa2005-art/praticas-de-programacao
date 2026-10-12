"""
Desafio 01 - Decorator de Cronometro
Nivel: Avancado

Objetivo:
    Escreva o decorator cronometro que mede e imprime quanto tempo
    uma funcao levou para executar.

Exemplo de uso:
    @cronometro
    def tarefa_lenta():
        time.sleep(1)

    tarefa_lenta()
    # Saida: "tarefa_lenta levou 1.00s"

Dicas:
    - Use "import time" e "import functools".
    - Um decorator e uma funcao que recebe outra funcao e retorna
      uma nova funcao (wrapper) que adiciona comportamento extra.
    - Use @functools.wraps(func) no wrapper para preservar metadados.
"""
import time
import functools


def cronometro(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # TODO: marque o tempo inicial, chame func, marque o tempo
        # final e imprima a diferenca antes de retornar o resultado
        pass
    return wrapper


@cronometro
def tarefa_lenta():
    time.sleep(1)


if __name__ == "__main__":
    tarefa_lenta()
