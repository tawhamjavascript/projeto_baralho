from PilhaException import PilhaException
from pilhaEncadeada import Pilha
from Carta import Carta
from random import shuffle
from BaralhoException import BaralhoException


class Baralho:
    def __init__(self, jogador: bool):
        self.__baralho = Pilha()  # cria um objeto pilha
        if not jogador:  # verifica se o baralho é do jogador se não é criado o baralho automaticamente
            self.__criar_baralho()

    def add_card(self, card: Carta) -> None:    # adiciona uma carta ao baralho
        self.__baralho.stack_up(card)

    def add_card_base(self, card: Carta) -> None:   # adiciona uma carta na base do baralho
        self.__baralho.stack_base(card)

    def draw_card(self) -> Carta:   # Pegar uma carta do baralho
        try:
            card = self.__baralho.unstack()
            return card

        except PilhaException:
            raise BaralhoException("O baralho não possui mais cartas")

    def reset_baralho(self) -> None:    # resetar o baralho
        self.__baralho.reset_stack()

    def is_empty(self) -> bool:     # verifica se está vazio
        return self.__baralho.is_empty()

    def __len__(self) -> int:   # retorna o tamanho do baralho
        return self.__baralho.length_deck()

    def __str__(self) -> str:   # retorna uma string com todos os elementos do baralho
        return self.__baralho.elements_in_stack()

    def __criar_baralho(self):  # monta o baralho automaticamente
        self.reset_baralho()
        naipe = ["Ouro", "Espada", "Paus", "Copas"]  # salva os tipos de cartas
        numeracao = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "valete", "dama", "rei"]  # guarda a numeração das cartas
        weight = 1  # guarda o peso das cartas
        baralho = list()
        for idx in range(len(naipe)):  # responsável por montar o baralho e guardar o baralho na classe carta
            for id in numeracao:
                baralho.append(Carta(naipe[idx], id, weight))
                weight += 1

            weight = 1

        shuffle(baralho)    # embaralha o baralho
        for card in baralho:
            self.add_card(card)
