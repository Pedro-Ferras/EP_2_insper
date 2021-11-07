import random, sys, time
from colorama import init, Fore, Back, Style

from domino.jogo import *
from domino.jogadores import *

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

            possivel = [str(x) for x in range(0, len(jogo['jogadores'][jogador_atual]))]
            indice_peca = input()
            if indice_peca not in possivel:
                print("Escolha um valor valido!")
                time.sleep(2)
            else:
                indice_peca = int(indice_peca)

        else:
            print("Jogador: " + str(jogador_atual) + " com " + str(len(jogo['jogadores'][jogador_atual])) + " peça(s)")

        jogador_atual += 1
        jogador_atual = jogador_atual % (numero_jogadores)


if __name__ == "__main__":
    main()
