from Baralho import Baralho
from Jogador import Jogador
from time import sleep
from PilhaException import PilhaException
from BaralhoVazioException import BaralhoVazio
from DeckException import DeckException
from Carta import Carta

class Batalha:
    def __init__(self, jogadores):
        self.__players = jogadores
        self.__baralho = Baralho()
        self.__cards = list()
        self.__temporary_cards = list()
        self.__index_player = -1


    def show_turn_player(self):
        index_player = (self.__index_player + 1) % self.number_of_players()

        return str(self.__players[index_player])

    def entregar_carta(self):
        try:
            index_player = (self.__index_player + 1) % self.number_of_players()
            card = self.__baralho.unstack()
            self.__players[index_player].stack_up(card)
            self.__index_player += 1
            return str(self.__players[index_player])

        except PilhaException:
            raise BaralhoVazio("O baralho já não possui mais cartas")

    def play_card(self):
        try:
            player_turn = (self.__index_player + 1) % self.number_of_players()

            card = self.__players[player_turn].unstack()
            self.__cards.append(card)
            string = str(card)
            self.__index_player += 1
            return string

        except PilhaException:
            raise DeckException(f"O jogador {self.__players[player_turn].nome} " +
                                f"não possui mais cartas.\n Portanto o {str(self.__players[player_turn])}")



    def number_of_players(self):
        return len(self.__players)

    def player_win_in_the_round(self) -> str:
        index_player = -1
        has_draw = False
        max_score = 0
        message = ""
        caracterOfVersus = " vs "

        for i in range(self.number_of_cards_plays()):
            if self.__cards[i].peso > max_score:
                max_score = self.__cards[i].peso
                index_player += 1

            elif self.__cards[i].peso == max_score:
                has_draw = True


        if has_draw:
            result = self.draw()
            return result

        else:
            while len(self.__temporary_cards) > 0:
                card = self.__temporary_cards.pop(0)
                self.__players[index_player].stack_base(card)
                message += str(card) + (caracterOfVersus if len(self.__temporary_cards) % 2 != 0 else " = empate\n")


            while self.number_of_cards_plays() > 0:
                card = self.__cards.pop(0)
                self.__players[index_player].stack_base(card)

                message += str(card) + (caracterOfVersus if self.number_of_cards_plays() % 2 != 0 else "")

            message += " = vitória do " + str(self.__players[index_player])
            return message

    def draw(self):
        message = ""
        for i in range(self.number_of_cards_plays()):
            card = self.__cards.pop(0)
            self.__temporary_cards.append(card)
            message += str(card) + (" vs " if i % 2 == 0 else " = empate\n")

        return message


        """
        jogadorWin = ""
        string_de_empate = ""
        if self.__cards[0] > self.__cards[1]:
            print(self.__cards[0].peso, self.__cards[1].peso)
            while self.number_of_cards_plays() > 0:
                self.__players[0].stack_base(self.__cards.pop(0))
                print("jogador 1 ganhador")

            jogadorWin = self.__players[0]

        elif self.__cards[1] > self.__cards[0]:
            print(self.__cards[0].peso, self.__cards[1].peso)


            while self.number_of_cards_plays() > 0:
                self.__players[1].stack_base(self.__cards.pop(0))
            print("jogador 2 ganhador")

            jogadorWin = self.__players[1]

        else:
            self.__temporary_cards += self.__cards
            self.__cards.clear()

        if len(self.__temporary_cards) > 0:
            for i in range(len(self.__temporary_cards)):
                card = self.__temporary_cards.pop(0)
                jogadorWin.stack_base(card)

                string_de_empate += card + (" vs " if i % 2 == 0 else "\n")

        message = string_de_empate + "O vencedor foi " + str(jogadorWin)

        return message
        
        
        
        
        """



    def number_of_cards_plays(self):
        return len(self.__cards)

if __name__ == "__main__":
    '''jogadores = [Jogador("edcleiton"), Jogador("jhon")]
    batalha = Batalha(jogadores)
    try:
        jogadores[0].stack_up(Carta("vermelho", "10", 20))
        batalha.play_card()
        batalha.play_card()

    except DeckException as error:
        print(error)'''

    """
    batalha.play_card()
    batalha.play_card()
    print(batalha.player_win_in_the_round())
    batalha.play_card()
    batalha.play_card()
    print(batalha.player_win_in_the_round())
    """


    """
    while True:
        try:
            batalha.entregar_carta()

        except:
            break
    while True:
        for i in range(2):
            print(batalha.play_card())

        print("------------------------------")
        valor = batalha.player_win_in_the_round()
        
        print(valor)
        print("------------------------------")
        if valor[0] == True:
            sleep(1)
"""
        













