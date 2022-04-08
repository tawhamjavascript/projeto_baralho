from Batalha import Batalha
from Jogador import Jogador
from BaralhoVazioException import BaralhoVazio
from time import sleep
from DeckException import DeckException
from RoundException import RoundException

players: list[Jogador] = list()  # uma lista de jogadores
PUXARCARTA = "p"

for i in range(2):
    # fazendo duas iterações perguntando o nome do usuário
    # e adicionando a lista de jogadores
    name = input(f"Digite o nome do jogador {i + 1}: ")
    players.append(Jogador(name))
    print(f"Bem vindo ao jogo { name } ")

batalha: Batalha = Batalha(players)

print("Embaralhando baralho .")
sleep(0.25) # colocando o código para dormir por 0.25 segundos
print("Embaralhando baralho ..")
sleep(0.25) # colocando o código para dormir por 0.25 segundos

print("Embaralhando baralho ...")

while True:
    # toda interação é entregue uma carta ao jogador
    # caso o baralho esteja vazio é levantado uma excessão
    try:
        information = batalha.entregar_carta()
        print("--------------------------------------------------")
        print(information)
        print("--------------------------------------------------")
        #sleep(1)


    except BaralhoVazio as error:
        print(error)
        print("--------------------------------------------------")
        break
        
print()
print()
count_of_turn = 1 # contador de turnos
print(f"\t\t\trodada {count_of_turn}")
print("-" * 50)

while True:
    # toda interação é pedido para o jogador jogar uma carta
    # até que haja um vencedor
    # quando o jogador não possui mais cartas é lançado uma excessão
    # quando se passaram muitas rodadas é lançado uma excessão
    # ambas as exceções informam o jogador vencedor e o jogo é terminado
    count_of_plays = 0
    count_of_turn += 1
    try:
        while count_of_plays < 2:
            turn = batalha.show_turn_player()
            print("turno do", turn)
            print()
            print("p - puxar carta")
            print()
            #option = input("Digite a opção: ")
            print()

            if "p" == PUXARCARTA:
                card = batalha.play_card()
                print("Carta: ", card)
                count_of_plays += 1
                print()

            else:
                print("Opção inválida, digite novamente!")

    except DeckException as error:
        print(error)
        break

    except RoundException as error:
        print(error)
        break

    player_win_round = batalha.player_win_in_the_round()
    print(player_win_round)

    print(f"\t\t\trodada { count_of_turn }")
    print("-" * 100)




















