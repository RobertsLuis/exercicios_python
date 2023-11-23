import unittest
import os
import sys

# Adiciona o diretório Solucoes ao sys.path
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
diretorio_solucoes = os.path.join(diretorio_atual, "..", "Solucoes")
sys.path.append(diretorio_solucoes)

from solucao_Q1 import expandir_intervalo


class TestExpandirRange(unittest.TestCase):
    def test_expandir_intervalo_valido(self):
        intervalos_teste = [
            ("A-C", "ABC"),
            ("Z-c", "Zabc"),
            ("c-Z", "Zabc"),
            ("A-a", "ABCDEFGHIJKLMNOPQRSTUVWXYZa"),
            ("4-11", "4, 5, 6, 7, 8, 9, 10, 11"),
            ("15-8", "8, 9, 10, 11, 12, 13, 14, 15")
        ]
        for intervalo_modelo, resultado_correto in intervalos_teste:
            with self.subTest(intervalo=intervalo_modelo):
                resultado = expandir_intervalo(intervalo_modelo)
                self.assertEqual(resultado, resultado_correto)

    def test_expandir_range_formato_invalido(self):
        with self.assertRaises(Exception) as contexto:
            expandir_intervalo("ac")

        self.assertEqual(
            str(contexto.exception),
            'O intervalo especificado está fora dos padrões aceitados \n"a-z"/"A-z"/"A-Z" ou "0-100" "20-0"',
        )


if __name__ == "__main__":
    unittest.main()
