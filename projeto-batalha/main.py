from Batalha import Batalha
from Jogador import Jogador
from BaralhoVazioException import BaralhoVazio
from time import sleep
from DeckException import DeckException
from RoundException import RoundException

players: list[Jogador] = list()  # uma lista de jogadores
PUXARCARTA = "p"
KEEPPLAYING = "S"
ENDGAME = "N"
continuePlaying = True # Variável que indica se o jogo vai continuar ou encerrar

for i in range(2):
    # fazendo duas iterações perguntando o nome do utilizador
    # e adicionando a lista de jogadores
    name = input(f"Digite o nome do jogador {i + 1}: ")
    players.append(Jogador(name))
    print(f"Bem vindo ao jogo { name } ")


def game():
    batalha: Batalha = Batalha(players)
    print("Embaralhando baralho .")
    sleep(0.30)  # colocando o código para dormir por 0,25 segundos
    print("Embaralhando baralho ..")
    sleep(0.30)  # colocando o código para dormir por 0,25 segundos
    print("Embaralhando baralho ...")

    while True:
        # toda a interação é entregue uma carta ao jogador
        # caso o baralho esteja vazio é levantado uma excessão
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
    count_of_turn = 0  # contador de turnos

    while True:
        # toda a interação é pedido para o jogador jogar uma carta
        # até que haja um vencedor
        # quando o jogador não possui mais cartas é lançado uma excessão
        # quando se passaram muitas rodadas é lançado uma excessão
        # ambas as exceções informam o jogador vencedor e o jogo é terminado
        count_of_plays = 0
        count_of_turn += 1
        try:
            while count_of_plays < 2:
                turn = batalha.show_turn_player()
                print(f"\t\t\trodada {count_of_turn}")
                print("-" * 100)
                print("turno do", turn)
                print("p - puxar carta")
                print()
                option = input("Digite a opção: ")
                print()
                if option == PUXARCARTA:
                    card = batalha.play_card()
                    print("Carta: ", card)
                    count_of_plays += 1
                    print()
                    sleep(0.36)

                else:
                    print("Opção inválida, digite novamente!")

        except DeckException as error:
            print(error)
            batalha.reset_game()  # resetar o jogo
            break

        except RoundException as error:
            print(error)
            batalha.reset_game()  # resetar o jogo
            break

        player_win_round = batalha.player_win_in_the_round()
        print(player_win_round)


while continuePlaying:
    game()  # chama a função para rodar o jogo
    while True:
        # Pergunta ao usuário se o jogo deve continuar ou não
        # Se o usuário responder uma opção inexistente é solicitado para digitar novamente

        print("Deseja continuar jogando? S - sim, N - não")
        option = input("Digite a opção: ")
        print()
        if option == KEEPPLAYING:
            break

        elif option == ENDGAME:
            continuePlaying = False
            break

        else:
            print("Opção incorreta, digite novamente")
