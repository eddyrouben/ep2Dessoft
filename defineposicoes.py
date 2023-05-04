def define_posicoes(linha, coluna, orientacao, tamanho):
    lista = []
    if orientacao == "vertical":
        for i in range(tamanho):
            lista.append([linha+i, coluna])
        return lista
    else:
        for i in range(tamanho):
            lista.append([linha, coluna+i])
        return lista