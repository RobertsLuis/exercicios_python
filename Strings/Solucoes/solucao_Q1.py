""" 
Questão:
https://www.codewars.com/kata/6512b3775bf8500baea77663
Given a string indicating a range of letters, return a string which includes all the letters in that range, including the last letter. 
Note that if the range is given in capital letters, return the string in capitals also!
"""

import re
def expandir_intervalo(intervalo):
    """Gera todos os elementos contidos no intervalo especificado 'x-y', em ordem crescente de valor
    
    **Sensível a letras maísculas e minúsculas 
    
    Args:
        range str: Uma string que deve seguir o padrão 'letra-letra' ou 'numero-numero'

    Returns:
        str: Todos os caracteres contidos no intervalo especificado
        
    """
    padraoLetras = re.compile(r'^[a-zA-Z]-[a-zA-Z]$')
    padraoNumeros = re.compile(r'^\d+-\d+$')

    if padraoLetras.match(intervalo):
        return __expandir_intervalo_letras(intervalo)
    elif padraoNumeros.match(intervalo):
        return __expandir_intervalo_numeros(intervalo)
    
    else:
        raise Exception('O intervalo especificado está fora dos padrões aceitados \n"a-z"/"A-z"/"A-Z" ou "0-100" "20-0"')

def __expandir_intervalo_letras(intervalo):
    inicio, fim = intervalo.split('-')
    if ord(inicio) > ord(fim):
        fim, inicio = inicio, fim
    expansao = ''.join(chr(i) for i in range(ord(inicio), ord(fim)+1))
    return re.sub(r'[^a-zA-Z]', '',expansao)

def __expandir_intervalo_numeros(intervalo):
    inicio, fim = intervalo.split('-')
    if int(inicio) > int(fim):
        fim, inicio = inicio, fim
    expansao = ', '.join(str(i) for i in range (int(inicio), int(fim)+1))
    return expansao