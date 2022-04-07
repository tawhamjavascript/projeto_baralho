from Batalha import Batalha
from Jogador import Jogador
from BaralhoVazioException import BaralhoVazio
from time import sleep
from DeckException import DeckException

jogadores: list[Jogador] = list()
PUXARCARTA = "p"

for i in range(2):
    name = input(f"Digite o nome do jogador {i + 1}: ")
    jogadores.append(Jogador(name))
    print(f"Bem vindo ao jogo { name } ")

batalha: Batalha = Batalha(jogadores)

print("Embaralhando baralho .")
sleep(0.25)
print("Embaralhando baralho ..")
sleep(0.25)

print("Embaralhando baralho ...")

while True:
    try:
        information = batalha.entregar_carta()
        print("--------------------------------------------------")
        print(information)
        print("--------------------------------------------------")
        sleep(1)


    except BaralhoVazio as error:
        print(error)
        print("--------------------------------------------------")


        break
print()
print()
contador_de_turno = 1
print(f"\trodada {contador_de_turno}")
print("-" * 50)

while True:
    contador_de_jogadas = 0
    contador_de_turno += 1
    try:
        while contador_de_jogadas < 2:
            turno = batalha.show_turn_player()
            print("turno do", turno)
            print("p - puxar carta")
            option = input("Digite a opção: ")

            if option == PUXARCARTA:
                card = batalha.play_card()
                print("Carta: ", card)
                contador_de_jogadas += 1
                print()

            else:
                print("Opção inválida, digite novamente!")

    except DeckException as error:
        print(error)
        break

    player_win_round = batalha.player_win_in_the_round()
    print(player_win_round)
    print()
    print(f"\trodada{contador_de_turno}")
    print("-" * 100)




















