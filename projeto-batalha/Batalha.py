from Baralho import Baralho
from PilhaException import PilhaException
from BaralhoVazioException import BaralhoVazio
from DeckException import DeckException
from RoundException import RoundException


class Batalha:
    def __init__(self, jogadores):
        self.__players = jogadores  # variável que vai guardar o array de jogadores
        self.__baralho = Baralho()  # criar uma instância de objeto
        self.__cards = list()   # cria uma array que vai guarda as cartas jogadas pelo jogadores
        self.__numberOfRounds = 0   # guarda os números de rounds disputados
        self.__temporary_cards = list()    # se houve empate as cartas serão guardadas nesse array
        self.__index_player = 0     # variavel que vai auxiliar na descoberta do turno do jogador

    def show_turn_player(self):
        # retorna o jogador que deve jogar nesse turno
        # se o número de rodadas for maior que 32, irá gerar uma exceção, e irá propagar outra exceção
        try:
            assert self.__numberOfRounds < 32
            index_player = self.__index_player % self.number_of_players()
            return str(self.__players[index_player])

        except AssertionError:
            raise RoundException(f"depois de {self.__numberOfRounds} rodadas {self.__player_win()}  ")

    def entregar_carta(self):
        # descobri qual jogador deve receber a carta
        # retira a carta do baralhp
        # entrega a carta para o jogador definido pela fórmula
        # e retorna as informações do jogador
        # se não tiver mais cartas no baralho é levantado uma exceção
        try:
            player_turn = self.__index_player % self.number_of_players()
            card = self.__baralho.unstack()
            self.__players[player_turn].stack_up(card)
            self.__index_player += 1
            message = f"O jogador {self.__players[player_turn].nome} recebeu a carta {str(card)}"
            return message

        except PilhaException:
            raise BaralhoVazio("O baralho não possui mais cartas")

    def play_card(self):
        # descobri qual jogador deve retirar a carta do seu baralho
        # guarda essa carta em uma lista
        # retorna uma string com as informações da carta
        # se o jogador não tiver mais cartar é levantada uma exceção e chamada a função player_win
        player_turn = None
        try:
            player_turn = self.__index_player % self.number_of_players()
            card = self.__players[player_turn].unstack()
            self.__cards.append(card)
            string = str(card)
            self.__index_player += 1
            return string

        except PilhaException:
            raise DeckException(f"{str(self.__players[player_turn])} não possui mais cartas. Portando {self.__player_win()}")

    def number_of_players(self):  # retorna a quantidade de jogadores
        return len(self.__players)

    def __player_win(self):
        # verifica qual jogador possui, o maior número de cartas
        # após isso monta uma mensagem informando qual jogador foi o vencedor
        # e retorna essa mensagem
        message = ""
        if self.__players[0].length_deck() > self.__players[1].length_deck():
            message += f"o vencedor foi  {str(self.__players[0])}"

        else:
            message += f"o vencedor foi {str(self.__players[1])}"

        return message

    def player_win_in_the_round(self) -> str:
        # verifica qual jogador ganhou a rodads
        # entrega as cartas apropriadamente
        # e retorna uma string informando o jogador vencedor
        # se der empate é montado uma mensagem de empate
        # guarda as cartas em uma lista de cartas temporárias
        # e retorna uma string informando o empate

        player_win = None
        string_of_draw = ""
        string_of_victory = ""
        if self.__cards[0] > self.__cards[1]:
            for i in range(self.number_of_cards_plays()):
                card = self.__cards.pop(0)
                string_of_victory += str(card) + (" vs " if i % 2 == 0 else " = ")
                self.__players[0].stack_base(card)

            player_win = self.__players[0]

        elif self.__cards[1] > self.__cards[0]:
            for i in range(self.number_of_cards_plays()):
                card = self.__cards.pop(0)
                string_of_victory += str(card) + (" vs " if i % 2 == 0 else " = ")
                self.__players[1].stack_base(card)

            player_win = self.__players[1]

        else:
            string_of_draw = "Ocorreu um empate. \n"
            for i in range(self.number_of_cards_plays()):
                card = self.__cards.pop(0)
                string_of_draw += ("\t --> " if i % 2 == 0 else "") + str(card) + (" vs " if i % 2 == 0 else " = empate\n")
                self.__temporary_cards.append(card)

        if len(self.__temporary_cards) > 0 and player_win is not None:
            for i in range(len(self.__temporary_cards)):
                card = self.__temporary_cards.pop(0)
                player_win.stack_base(card)
                string_of_draw += str(card) + (" vs " if i % 2 == 0 else " = empate\n")

        message = string_of_draw + string_of_victory + ("O vencedor foi " + str(player_win) if player_win else "\n")
        self.__numberOfRounds += 1

        return message

    def number_of_cards_plays(self):  # retorna a quantidade de cartas
        return len(self.__cards)
