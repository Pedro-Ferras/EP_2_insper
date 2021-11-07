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

def print_local(local, selecionavel=[]):

    if (selecionavel):
        for domino_index in range(0, len(local)):
            if domino_index in selecionavel:
                print("  *  ", end=" ")
            else:
                print("     ", end=" ")
        
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