def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    lista = []
    if orientacao == "vertical":
        for i in range(tamanho):
            lista.append([linha+i, coluna])
    else:
        for i in range(tamanho):
            lista.append([linha, coluna+i])

    if nome_navio in frota:
        frota[nome_navio].append(lista)
    else:
        frota[nome_navio] = []
        frota[nome_navio].append(lista)
    return frota