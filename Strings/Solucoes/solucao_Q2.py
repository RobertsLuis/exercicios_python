""" 
Questão:
https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true
You are given a string, line width and paragraph height.
Your task is to wrap the string into paragraph(s).

**You can't return a half word
"""


def organizar_texto_em_paragrafo(texto, largura_linha, altura_paragrafo):
    """Quebra os textos em linhas e paragrafos

    Args:
        texto str: Texto que sofrerá a organização
        largura_linha str: Limite de letras em cada linha
        altura_paragrafo str: Limite de linhas em cada paragro
    Returns:
        str: Texto organizado em linhas e paragrafos

    """
    palavras = texto.split()
    info_palavras = [(palavra, len(palavra)) for palavra in palavras]
    linhas = [""]
    for palavra, tamanho_palavra in info_palavras:
        tamanho_linha_atual = len(linhas[-1])
        if tamanho_linha_atual + tamanho_palavra <= largura_linha:
            linhas[-1] += f" {palavra}"
        else:
            linhas.append(
                f"{palavra}"
                if len(linhas) % altura_paragrafo > 0
                else f"\n{palavra.capitalize()}"
            )

    return "\n".join(linhas).replace(" ", "", 1)
