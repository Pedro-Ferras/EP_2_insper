import random, sys
from colorama import init, Fore, Back, Style


def cria_pecas():
    pecas = [
	    [0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6],
	    [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], 
        [2, 2], [2, 3], [2, 4], [2, 5], [2, 6],
        [3, 3], [3, 4], [3, 5], [3, 6],
        [4, 4], [4, 5], [4, 6],
        [5, 5], [5, 6],
        [6, 6]
    ]

    random.shuffle(pecas)

    return pecas


def inicia_jogo(numero_jogadores, pecas_possiveis):

    jogo = {'jogadores': {}, 'monte': {}, 'mesa': []}

    pecas_restantes = pecas_possiveis

    for x in range(0, numero_jogadores):
        jogo['jogadores'][x] = random.sample(pecas_possiveis, 7)

        pecas_restantes = [domino for domino in pecas_restantes if (domino not in jogo['jogadores'][x])]

    jogo['monte'] = pecas_restantes

    return jogo


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


def print_local(local, selecionavel=[]):

    if (selecionavel):
        for domino_index in range(0, len(local)):
            if domino_index in selecionavel:
                print("  *   ", end="")
            else:
                print("    ", end="")
        
        print("")
    for domino in local:
        print("[", end="")
        for num in range(0, 2):
            if (domino[num]) == 0:
                print(Fore.LIGHTBLACK_EX + "0", end="")
            elif domino[num] == 1:
                print(Fore.BLUE + "1", end="")
            elif domino[num] == 2:
                print(Fore.YELLOW + "2", end="")
            elif domino[num] == 3:
                print(Fore.GREEN + "3", end="")
            elif domino[num] == 4:
                print(Fore.MAGENTA + "4", end="")
            elif domino[num] == 5:
                print(Fore.RED + "5", end="")
            elif domino[num] == 6:
                print(Fore.CYAN + "6", end="")

            print(Fore.WHITE, end="")
            if (num == 0):
                print("|", end="")
        print("]", end=" ")
    print("")
    if (selecionavel):
        for domino_index in range(0, len(local)):
            print("  " + str(domino_index) + "  ", end=" ")
            
    print("")


def soma_pecas(jogador):

    total = 0

    for domino in jogador:
        total += sum(domino)

    return total

def jogada_aleatoria(jogo, indice_jogador):
    return None

def main():

    init()

    print("==> Design de Software ")
    print("Insper Dominó")

    print("Bem-vindo(a) ao jogo de Dominó! O objetivo desse jogo é ficar sem peças na sua mão antes dos outros jogadores.")
    print("Vamos começar!!!")

    print("Quantos jogadores? (2-4) ")
    numero_jogadores = int(input())

    jogo = inicia_jogo(numero_jogadores, cria_pecas())

    jogador_atual = random.randint(0, numero_jogadores - 1)

    while(verifica_ganhador(jogo['jogadores']) == -1):
        print("MESA:")
        print_local(jogo['mesa'])

        if (jogador_atual == 0):
            print("Jogador: Você com " + str(len(jogo['jogadores'][jogador_atual])) + " peça(s)")
            print_local(jogo['jogadores'][jogador_atual], posicoes_possiveis(jogo['mesa'], jogo['jogadores'][jogador_atual]))

            print("Escolha a peça:", end=" ")

            indice_peca = int(input())

        else:
            print("Jogador: " + str(jogador_atual) + " com " + str(len(jogo['jogadores'][jogador_atual])) + " peça(s)")

        jogador_atual += 1
        jogador_atual = jogador_atual % (numero_jogadores)


if __name__ == "__main__":
    main()
