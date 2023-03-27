def distancia_hamming(a, b):
    """
    Recebe duas strings de mesmo tamanho, a e b.
    Devolve a distância de Hamming entre as duas.
    """
    i = 0
    d = 0
    while i < len(a):
        if a[i] != b[i]:
            d += 1
        i += 1
    return d

def minima_distancia(alvo, candidatos):
    """
    Recebe uma string alvo e uma lista de strings candidatas.
    Devolve um par contendo a string candidata com menor distância
    de Hamming até o alvo, além da distância.

    Exemplo de uso: sequencia, valor = minima_distancia(alvo, candidatos)
    """
    minimo = len(candidatos[0]) + 2
    candidato_min = ""
    for canditado in candidatos:
        d = distancia_hamming(alvo, canditado)
        if d < minimo:
            minimo = d
            candidato_min = canditado
    return candidato_min, minimo

def janela(sequencia, indice_inicial, tamanho_janela):
    """
    Recebe uma string, um índice inicial e o tamanho da janela.
    Devolve uma string correspondente à janela da sequência começando
    no índice inicial fornecido.

    Exemplo: janela('ABCDEFGHIJ', 2, 3) devolve 'CDE'.
    """
    janela = sequencia[indice_inicial:(indice_inicial+tamanho_janela)]
    
    return janela


def distancia_janela(a, b, indice_inicial, tamanho_janela):
    """
    Recebe duas strings a e b, um índice inicial e o tamanho da janela.
    Devolve a distância de Hamming entre as respectivas janelas
    das strings a e b.

    Exemplo: distancia_janela('AAABBB', 'AABABB', 1, 4) devolve 2,
    que é a distância entre 'AABB' e 'ABAB'
    """
    janelaA = janela(a, indice_inicial, tamanho_janela)
    janelaB = janela(b, indice_inicial, tamanho_janela)

    d = distancia_hamming(janelaA, janelaB)
    return d

def diferencas(a, b, tamanho_janela):
    """
    Recebe duas sequências (strings) a e b e o tamanho da janela.
    Devolve uma lista com todas as posições em que as janelas de a e de b
    apresentam diferença SIGNIFICATIVa, isto é, de pelo menos 1/3 do tamanho
    da janela.
    """
    i = 0
    dif = []
    dif2 = []
    while i < len(a):
        d =  distancia_janela(a, b, i, tamanho_janela)
        if d >= (tamanho_janela/3):
           dif.append(i)
           #dif2.append(janela(a, i, tamanho_janela))
           #dif2.append(janela(b, i, tamanho_janela))
           #dif2.append(d)
        i += tamanho_janela

    return dif


