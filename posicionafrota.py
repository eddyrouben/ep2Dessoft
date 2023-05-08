def posiciona_frota(frota):
    tabuleiro = [[0 for i in range(10)]for j in range(10)]

    for posicao_barcos in frota.values():
        for barcos in posicao_barcos:
            for cordenada in barcos:
                tabuleiro[cordenada[0]][cordenada[1]] = 1
    return tabuleiro