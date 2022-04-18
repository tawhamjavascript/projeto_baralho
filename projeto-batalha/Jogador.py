from Carta import Carta
from Baralho import Baralho
from BaralhoException import BaralhoException


class Jogador:
    def __init__(self, name: str):
        self.__name = name  # guarda o nome do jogador
        self.__deck = Baralho(True)  # criar um objeto com o parâmetro true informando que é um jogador

    @property
    def nome(self):  # retorna o nome do jogador
        return self.__name

    def add_card_in_the_head(self, card: Carta) -> None:  # adicionar carta no deck
        self.__deck.add_card(card)

    def play_card(self) -> Carta:   # retira uma carta do deck
        try:
            card = self.__deck.draw_card()
            return card

        except BaralhoException:
            raise BaralhoException("O baralho não possui mais cartas")

    def add_card_in_the_base(self, card: Carta) -> None:    # adiciona uma carta na base do deck
        self.__deck.add_card_base(card)

    def reset_deck(self):   # esvazia o deck
        self.__deck.reset_baralho()

    def __len__(self):  # retorna o tamanho do deck
        return len(self.__deck)

    def __str__(self):  # retorna uma string com o nome e o tamanho do deck do jogador
        return f"jogador { self.__name } possui { self.__len__() } cartas"












