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
    """ 
        A cada interação é solicitado o nome do usuário
        é criado um objeto da classe jogador 
        passa o nome como argumento do objeto
        é mostrado uma mensagem de bem vindo ao jogador
        se o usuário informar um nome inválido é solicitador a digitação do nome novamente
        
    """
    while True:
        name = input(f"Digite o nome do jogador { i + 1 }: ")
        if name:
            players.append(Jogador(name))
            print(f"Bem vindo ao jogo { name } ")
            break

        print("Nome inválido digite novamente")


def game():
    print()
    batalha: Batalha = Batalha(players)  # cria um objeto da classe batalha
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
        """ 
            toda a interação é entregue uma carta ao jogador
            caso o baralho esteja vazio é levantado uma excessão
            informa quantas cartas cada jogador possui
            
        """

        try:
            batalha.entregar_carta()

        except BaralhoException:
            break

    print()
    print(f"O { players[0] }")
    print(f"O { players[1] }")
    print()

    while True:
        """
         toda a interação os jogadores jogam uma carta
         verifica quem foi o ganhador da rodada
         até que haja um vencedor da partida
         quando o jogador não possui mais cartas é lançado uma excessão
         quando se passaram muitas rodadas é lançado uma excessão
         ambas as exceções informam o jogador vencedor e o deck é recetado
         quando a rodada está terminada é pedido para o usuário aperta a tecla enter para continuar
         caso o jogador informe uma opção inexistente é solicitado novamente a submissão da opção
        """

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
    """
        Em toda itenração vai ser chamado a função game
        solicitado ao usuário se ele quer continuar ou não
        se a resposta for sim o código é rodado novamente
        se não o jogo termina
        se o usuário informar uma opção inválida é solicitado novamente para ele digitar a opção
    
    """
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
