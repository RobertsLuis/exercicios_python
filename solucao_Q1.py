""" 
Questão:
https://www.codewars.com/kata/6512b3775bf8500baea77663
Given a string indicating a range of letters, return a string which includes all the letters in that range, including the last letter. 
Note that if the range is given in capital letters, return the string in capitals also!
"""

import re
def expandir_range(intervalo):
    """Gera todas as letras contidas no intervalo especificado 'x-y'
    
    **Sensível a letras maísculas e minúsculas
    
    Args:
        range str: 'a-z'

    Returns:
        str: todas as letras dentro do range especificado
        
    """
    padrao = re.compile(r'^[a-zA-Z]-[a-zA-Z]$')
    if not(padrao.match(intervalo)):
        raise Exception('O range especificado está fora do padrão "a-z"/"A-z"/"A-Z"')
    inicio, fim = intervalo.split('-')
    if ord(inicio) > ord(fim):
        fim, inicio = inicio, fim
    expansao = ''.join(chr(i) for i in range(ord(inicio), ord(fim)+1))
    return re.sub(r'[^a-zA-Z]', '',expansao)

print(expandir_range('z-Z'))