import sequencias


def mensagem_padrao(nome_da_funcao):
    return "Resultado errado na função " + nome_da_funcao


def teste_unidade_01_distancia_hamming():
    mensagem = mensagem_padrao("distancia_hamming")
    tamanho = 10
    A = "1" * tamanho
    B = "0" * tamanho
    assert sequencias.distancia_hamming(A, B) == tamanho, mensagem
    A = "000"
    B = A
    assert sequencias.distancia_hamming(A, B) == 0, mensagem


def teste_unidade_02_minima_distancia():
    mensagem = mensagem_padrao("minima_distancia")
    alvo = "ACATT"
    candidatos = ["GCGAT", "ACGGT", "ACGTT"]
    esperado = "ACGTT"
    valor_esperado = 1

    sequencia, valor = sequencias.minima_distancia(alvo, candidatos)
    assert sequencia == esperado, mensagem
    assert valor == valor_esperado, mensagem

    candidatos.append(alvo)
    sequencia, valor = sequencias.minima_distancia(alvo, candidatos)
    assert sequencia == alvo, mensagem
    assert valor == 0, mensagem


def teste_unidade_03_janela():
    mensagem = mensagem_padrao("janela")
    assert sequencias.janela("ABCDEFGHIJ", 2, 3) == "CDE", mensagem


def teste_unidade_04_distancia_janela():
    mensagem = mensagem_padrao("distancia_janela")
    assert sequencias.distancia_janela("AAABBB", "AABABB", 1, 4) == 2, mensagem


# apenas para a parte 2 da tarefa
def teste_unidade_05_diferencas():
    mensagem = mensagem_padrao("diferencas")
    A = "OOOXXXOOOXXX"
    B = "OOOXOXOOOXXO"
    tam_janela = 3
    assert sequencias.diferencas(A, B, tam_janela) == [3, 9], mensagem
