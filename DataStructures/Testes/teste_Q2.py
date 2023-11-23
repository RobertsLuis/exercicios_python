import unittest
import os
import sys

# Adiciona o diretório Solucoes ao sys.path
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
diretorio_solucoes = os.path.join(diretorio_atual, "..", "Solucoes")
sys.path.append(diretorio_solucoes)

from solucao_Q2 import informacoes_quantitativas

class TestExpandirRange(unittest.TestCase):
    def test_informacoes_quantitativas(self):
        listas_teste = [
          ([-3, -2, -1, 3, 4, -5, -5, 5, -1, -5], [10, 7, 5, [[-5], 3]]),
          ([5, -1, 1, -1, -2, 5, 0, -2, -5, 3], [10, 7, 4, [[-2, -1, 5], 2]]),
          ([4, 4, 2, -3, 1, 4, 3, 2, 0, -5, 2, -2, -2, -5], [14, 8, 4, [[2, 4], 3]])
        ]
        for lista_modelo, resultado_correto in listas_teste:
            with self.subTest(lista=lista_modelo):
                resultado = informacoes_quantitativas(lista_modelo)
                self.assertEqual(resultado, resultado_correto)

if __name__ == "__main__":
    unittest.main()
