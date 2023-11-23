import unittest
import os
import sys

# Adiciona o diretório Solucoes ao sys.path
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
diretorio_solucoes = os.path.join(diretorio_atual, "..", "Solucoes")
sys.path.append(diretorio_solucoes)

from solucao_Q1 import expandir_range


class TestExpandirRange(unittest.TestCase):
    def test_expandir_range_valido(self):
        intervalos_teste = [
            ("A-C", "ABC"),
            ("Z-c", "Zabc"),
            ("c-Z", "Zabc"),
            ("A-a", "ABCDEFGHIJKLMNOPQRSTUVWXYZa"),
        ]
        for intervalo_modelo, resultado_correto in intervalos_teste:
            with self.subTest(intervalo=intervalo_modelo):
                resultado = expandir_range(intervalo_modelo)
                self.assertEqual(resultado, resultado_correto)

    def test_expandir_range_formato_invalido(self):
        with self.assertRaises(Exception) as contexto:
            expandir_range("ac")

        self.assertEqual(
            str(contexto.exception),
            'O intervalo especificado está fora do padrão "a-z"/"A-z"/"A-Z"',
        )


if __name__ == "__main__":
    unittest.main()
