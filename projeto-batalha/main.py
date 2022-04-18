from Batalha import Batalha
from Jogador import Jogador
from time import sleep
from RoundException import RoundException
from BaralhoException import BaralhoException


players: list[Jogador] = list()  # uma lista de jogadores
KEEPPLAYING = "S"
ENDGAME = "N"
CONTINUAR = ""
continuePlaying = True  # Variável que indica se o jogo vai continuar ou encerrar

for i in range(2):
    # fazendo duas iterações perguntando o nome do utilizador
    # e adicionando a lista de jogadores
    name = input(f"Digite o nome do jogador { i + 1 }: ")
    players.append(Jogador(name))
    print(f"Bem vindo ao jogo { name } ")


def game():
    print()
    batalha: Batalha = Batalha(players)
    print(f"O baralho possui { batalha.length_baralho() } cartas")
    print("Embaralhando baralho .")
    sleep(0.30)  # colocando o código para dormir por 0,25 segundos
    print("Embaralhando baralho ..")
    sleep(0.30)  # colocando o código para dormir por 0,25 segundos
    print("Embaralhando baralho ...")
    print("entregando às cartas.")
    sleep(0.40)   # colocando o código para dormir por 0,40 segundos
    print("entregando às cartas..")
    sleep(0.40)   # colocando o código para dormir por 0,40 segundos
    print("entregando às cartas...")

    while True:
        # toda a interação é entregue uma carta ao jogador
        # caso o baralho esteja vazio é levantado uma excessão

        try:
            batalha.entregar_carta()

        except BaralhoException:
            break

    print()
    print(f"O { players[0] }")  # informar ao jogador quantas cartas ele possui depois da distribuição das cartas
    print(f"O { players[1] }")
    print()

    while True:
        # toda a interação os jogadores jogam uma carta
        # até que haja um vencedor
        # quando o jogador não possui mais cartas é lançado uma excessão
        # quando se passaram muitas rodadas é lançado uma excessão
        # ambas as exceções informam o jogador vencedor e o deck é recetado
        # quando a rodada está terminada é pedido para o usuário aperta a tecla enter para continuar

        try:
            print(f"\t\t\t{batalha.show_rounds()} rodadas")
            print("-" * 100)
            batalha.play_card()

        except BaralhoException as error:
            print(error)
            batalha.reset_game()  # resetar o jogo
            break

        except RoundException as error:
            print(error)
            batalha.reset_game()  # resetar o jogo
            break

        player_win_round = batalha.player_win_in_the_round()  # chama a função que informa quem ganhou a rodada
        print(player_win_round)
        print()

        while True:
            print(" DIGITE ENTER PARA CONTINUAR".rjust(50, "="), "=" * 20)
            option = input()
            print()
            if option == CONTINUAR:
                break

            print("Opção inexistente digite novamente")
            print()


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
