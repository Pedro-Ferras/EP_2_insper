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

        fazer_jogada(jogo, jogador_atual, jogador_atual != 0)

        jogador_atual += 1
        jogador_atual = jogador_atual % (numero_jogadores)

    vencedor = verifica_ganhador(jogo['jogadores'])
    if (vencedor == 0):
        print("Você ganhou, parabéns!")
    else:
        print("Vencedor: Jogador " + str(verifica_ganhador(jogo['jogadores'])))

if __name__ == "__main__":
    main()
