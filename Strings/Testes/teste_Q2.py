import unittest
import os
import sys

# Adiciona o diretório Solucoes ao sys.path
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
diretorio_solucoes = os.path.join(diretorio_atual, "..", "Solucoes")
sys.path.append(diretorio_solucoes)

from solucao_Q2 import organizar_texto_em_paragrafo


class TestExpandirRange(unittest.TestCase):
    def test_organizar_texto(self):
        textos_teste = [
            (("Cinco Cinco Cinco Cinco Cinco Cinco Cinco Cinco", 12, 2), "Cinco Cinco\nCinco Cinco\n\nCinco Cinco\nCinco Cinco"),
            (("Cinco Cinco Cinco Cinco cinco", 12, 2), "Cinco Cinco\nCinco Cinco\n\nCinco")
        ]
        for argumentos_modelo, resultado_correto in textos_teste:
            with self.subTest(textos=argumentos_modelo):
                texto, linha, paragrafo = argumentos_modelo
                resultado = organizar_texto_em_paragrafo(texto, linha, paragrafo)
                self.assertEqual(resultado, resultado_correto)

if __name__ == "__main__":
    unittest.main()
