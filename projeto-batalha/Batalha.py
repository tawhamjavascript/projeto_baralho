from Baralho import Baralho
from RoundException import RoundException
from BaralhoException import BaralhoException


class Batalha:
    def __init__(self, jogadores):
        self.__players = jogadores  # variável que vai guardar o array de jogadores
        self.__baralho = Baralho(False)  # criar uma instância de objeto
        self.__cards = list()   # cria uma array que vai guarda as cartas jogadas pelo jogadores
        self.__numberOfRounds = 0  # guarda os números de rounds disputados
        self.__temporary_cards = list()    # se houve empate as cartas serão guardadas nesse array
        self.__index_player = 0     # variavel que vai auxiliar na descoberta do turno do jogador
        self.__histoty_of_draw = list()  # array que contém os históricos de empate

    def length_baralho(self):  # retorna o tamanho do baralho
        return len(self.__baralho)

    def show_rounds(self) -> int:
        """
            A cada chamada do método o número de rodadas é somado mais 1
            é checado se o número de rodadas é menor que um valor determinado
            se for maior é levantado uma excessão do tipo assert
            sendo transmitida uma excessão do tipo RoundException

            return: um inteiro representando o número de rodadas
        """

        try:
            assert self.__numberOfRounds < 33
            self.__numberOfRounds += 1
            return self.__numberOfRounds

        except AssertionError:
            raise RoundException(f"depois de {self.__numberOfRounds} rodadas {self.__player_win()}  ")

    def entregar_carta(self) -> None:
        """
            É descoberto o jogador que vai receber a carta pela formula de lista circular
            é retirada uma carta do baralho
            entrega a carta ao jogador determinado
            e o index é somado mais um
            caso o baralho não possua mais cartas é levantada uma excessão do tipi BaralhoException
            esse erro é tratado dando um raise de um erro BaralhoException



        """
        # descobri qual jogador deve receber a carta
        # retira a carta do baralhp
        # entrega a carta para o jogador definido pela fórmula
        # se não tiver mais cartas no baralho é levantado uma exceção
        try:
            player_turn = self.__index_player % self.number_of_players()
            card = self.__baralho.draw_card()
            self.__players[player_turn].add_card_in_the_head(card)
            self.__index_player += 1

        except BaralhoException:
            raise BaralhoException("Não possui mais cartas")

    def play_card(self):
        """
            faz um for para cada jogador poder jogar a carta
            guarda essa carta em uma lista
            cria uma variável index que só é usada quando o jogador fica sem cartas
            se o jogador não tiver mais cartar é levantada uma exceção e chamada a função player_win

        """
        index = 0
        try:
            for player in self.__players:
                card = player.play_card()
                self.__cards.append(card)
                index += 1

        except BaralhoException:
            raise BaralhoException(f"O jogador {self.__players[index].nome} não possui mais cartas. Portando {self.__player_win()}")

    def number_of_players(self):  # retorna a quantidade de jogadores
        return len(self.__players)

    def __player_win(self) -> str:
        """
            verifica qual jogador possui, o maior número de cartas
            após isso monta uma mensagem informando qual jogador foi o vencedor
            e retorna essa mensagem

        """
        if len(self.__players[0]) > len(self.__players[1]):
            return f"o vencedor foi o {str(self.__players[0])}"

        return f"o vencedor foi o {str(self.__players[1])}"

    def player_win_in_the_round(self) -> str:
        """
        Verifica qual jogador ganhou a rodads
        entrega as cartas apropriadamente
        e retorna uma string informando o jogador vencedor
        se der empate é montado uma mensagem de empate
        guarda as cartas em uma lista de cartas temporárias
        a mensagem de empate é guardada numa lista
        e retorna uma string informando o empate
        caso na rodada anterior houve um empate é retornado uma string com o histórico de empates
        e o ganhador da rodada.

        """

        player_win = None
        string_general = ""
        history_of_draw = ""

        if self.__cards[0] > self.__cards[1]:
            string_general = f"({len(self.__players[0])} cartas) {self.__players[0].nome} {self.__cards[0]}"
            string_general += f" vs {self.__cards[1]} {self.__players[1].nome} ({len(self.__players[1])} cartas)\n"
            for i in range(self.number_of_cards_plays()):
                card = self.__cards.pop(0)
                self.__players[0].add_card_in_the_base(card)

            player_win = self.__players[0]

        elif self.__cards[1] > self.__cards[0]:
            string_general = f"({len(self.__players[0])} cartas) {self.__players[0].nome} {self.__cards[0]}"
            string_general += f" vs {self.__cards[1]} {self.__players[1].nome} ({len(self.__players[1])} cartas)\n"
            for i in range(self.number_of_cards_plays()):
                card = self.__cards.pop(0)

                self.__players[1].add_card_in_the_base(card)

            player_win = self.__players[1]

        else:
            string_general += f"({len(self.__players[0])} cartas) {self.__players[0].nome} {self.__cards[0]}"
            string_general += f" vs {self.__cards[1]} {self.__players[1].nome} ({len(self.__players[1])} cartas) = empate\n"
            self.__histoty_of_draw.append(string_general)
            for i in range(self.number_of_cards_plays()):
                card = self.__cards.pop(0)
                self.__temporary_cards.append(card)

        if len(self.__temporary_cards) > 0 and player_win is not None:
            for i in range(len(self.__temporary_cards)):
                card = self.__temporary_cards.pop(0)
                player_win.add_card_in_the_base(card)

            history_of_draw = "".join(self.__histoty_of_draw)
            self.__histoty_of_draw.clear()

        message = history_of_draw+string_general+(f" o vencedor foi {player_win}" if player_win is not None else "")
        return message

    def number_of_cards_plays(self):  # retorna a quantidade de cartas
        return len(self.__cards)

    def reset_game(self):   # reseta o deck dos jogadores
        for i in range(self.number_of_players()):
            self.__players[i].reset_deck()

