import random, sys

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

def print_mesa(mesa):
    print("Em Jogo")

def main():
    print("==> Design de Software ")
    print("Insper Dominó")

    print("Bem-vindo(a) ao jogo de Dominó! O objetivo desse jogo é ficar sem peças na sua mão antes dos outros jogadores.")
    print("Vamos começar!!!")

    print("Quantos jogadores? (2-4)\n")
    numero_jogadores = int(input())

    jogo = inicia_jogo(numero_jogadores, cria_pecas())

    print(jogo['jogadores'])

    while(verifica_ganhador(jogo['jogadores']) == -1):
        print_mesa(jogo['mesa'])

if __name__ == "__main__":
    main()