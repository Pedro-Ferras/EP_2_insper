import time

def verifica_ganhador(jogadores):
    for x in range(0, len(jogadores)):
        if not jogadores[x]:
            return x
    return -1


def posicoes_possiveis(mesa, jogador):

    possiveis = []
    
    if mesa:
        inicial = mesa[0][0]
        final = mesa[-1][1]

        for domino in jogador:
            for num in range(0, 1):
                if domino[num] == inicial or domino[num] == final:
                    possiveis.append(jogador.index(domino))
                    break

    else:
        possiveis = range(0, len(jogador))
    
    return possiveis

def soma_pecas(jogador):

    total = 0

    for domino in jogador:
        total += sum(domino)

    return total

def inserir_peca(mesa, peca):
    time.sleep(1)
    if mesa:
        start = mesa[0]
        end = mesa[-1]
    else:
        mesa.append(peca)

def jogada_aleatoria(jogo, indice_jogador):
    return None