import time, random

from domino.jogo import *

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
            for num in range(0, 2):
                if domino[num] == inicial or domino[num] == final and jogador.index(domino) not in possiveis:
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
        
        if start[0] == peca[0]:
            peca.reverse()
            mesa.insert(0, peca)
        elif (start[0] == peca[1]):
            mesa.insert(0, peca)
        elif (end[1] == peca[0]):
            mesa.append(peca)
        elif (end[1] == peca[1]):
            peca.reverse()
            mesa.append(peca)

    else:
        mesa.append(peca)

def jogada_aleatoria(jogo, indice_jogador):
    return None

def fazer_jogada(jogo, jogador_atual, aleatoria=False):

    if not aleatoria:
        print("Jogador: Você com " + str(len(jogo['jogadores'][jogador_atual])) + " peça(s)")
        print_local(jogo['jogadores'][jogador_atual], posicoes_possiveis(jogo['mesa'], jogo['jogadores'][jogador_atual]))
    else:
        print("Jogador: " + str(jogador_atual) + " com " + str(len(jogo['jogadores'][jogador_atual])) + " peça(s)")

    possivel = posicoes_possiveis(jogo['mesa'], jogo['jogadores'][jogador_atual])

    pular_vez = False

    while not possivel:
        print("Não tem peças possíveis. PEGANDO DO MONTE!")
        time.sleep(0.5)
        if not aleatoria:
            print("pressione ENTER")
            input()

        if (jogo['monte']):
            escolhida = random.choice(jogo['monte'])
            jogo['monte'].remove(escolhida)
            jogo['jogadores'][jogador_atual].append(escolhida)

            possivel = posicoes_possiveis(jogo['mesa'], jogo['jogadores'][jogador_atual])
        else:
            possivel = True
            pular_vez = True
        if not aleatoria:
            print_local(jogo['jogadores'][jogador_atual], posicoes_possiveis(jogo['mesa'], jogo['jogadores'][jogador_atual]))


    if not aleatoria:
        print("Escolha a peça:", end=" ")
        indice_peca = input()
    else:
        indice_peca = random.choice(possivel)
        print("Colocou: ", end="")
        print_domino(jogo['jogadores'][jogador_atual][indice_peca])
        print("\n", end="")

    if not pular_vez:
        
        if aleatoria:
            inserir_peca(jogo['mesa'], jogo['jogadores'][jogador_atual][indice_peca])
            jogo['jogadores'][jogador_atual].remove(jogo['jogadores'][jogador_atual][indice_peca])
            time.sleep(0.7)
        else:
            if indice_peca not in [str(x) for x in possivel]:
                print("Escolha um valor valido!")
                time.sleep(0.5)
            else:
                indice_peca = int(indice_peca)
                inserir_peca(jogo['mesa'], jogo['jogadores'][jogador_atual][indice_peca])

                jogo['jogadores'][jogador_atual].remove(jogo['jogadores'][jogador_atual][indice_peca])
