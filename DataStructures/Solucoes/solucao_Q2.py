""" 
Questão:
https://www.codewars.com/kata/55f95dbb350b7b1239000030
Given a string indicating a range of letters, return a string which includes all the letters in that range, including the last letter. 
Note that if the range is given in capital letters, return the string in capitals also!
"""

from collections import Counter

def informacoes_quantitativas(lista):
    """Obtem informações quntitativas a partir da lista de inteiros recebida. 

    Args:
        lista (list): Lista de inteiros de que serão extraidas as informações

    Returns:

        lista:

                1º Elemento - (int) Total de números da lista

                2º Elemento - (int) Quantidade de numeros únicos na lista

                3º Elemento - (int) Quantidade de elementos que aparecem apenas uma vez na lista

                4º Elemento - (list) 

                    1º Elemento - Lista com os elementos que mais apareceram na lista

                    2º Elemento - Quantidade de vezes que esses elementos de maior frequência apareceram
    """
    contagem = Counter(lista)
    maior_numero_aparicoes = max(contagem.values())
    elementos_mais_freq = sorted(set([elemento for elemento in lista if contagem[elemento]==maior_numero_aparicoes]))
    return [
        len(lista), 
        len(set(lista)), 
        len([x for x in lista if contagem[x]==1]),
        [elementos_mais_freq,maior_numero_aparicoes]
    ]

