def afundados(frota, tabuleiro):
    i = 0
    afundado = 0
    for posicao_barcos in frota.values():
        for barcos in posicao_barcos:
                for cordenada in barcos:
                    if frota["porta-aviões"] == posicao_barcos:
                        if tabuleiro[cordenada[0]][cordenada[1]] == 'X':
                            i += 1
                        if i == 4:
                            afundado += 1
                            i = 0
                    if frota["submarino"] == posicao_barcos:
                        if tabuleiro[cordenada[0]][cordenada[1]] == 'X':
                            i += 1
                        if i == 1:
                            afundado += 1
                            i = 0
                    if frota["navio-tanque"] == posicao_barcos:
                        if tabuleiro[cordenada[0]][cordenada[1]] == 'X':
                            i += 1
                        if i == 3:
                            afundado += 1
                            i = 0
                            
                    if frota["contratorpedeiro"] == posicao_barcos:
                        if tabuleiro[cordenada[0]][cordenada[1]] == 'X':
                            i += 1
                        if i == 2:
                            afundado += 1
                            i = 0
                    
                i = 0
    return afundado