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

    def draw_card(self) -> Carta:
        """
            retira uma carta da pilha
            e retorna essa carta
            se não tiver carta na pilha é levantado uma excessão de PilhaException
            e dá uma raise de BaralhoException

        """
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

    def __criar_baralho(self) -> None:
        """"
            chama a função reset_baralho para esvaziar o baralho
            é construído uma lista com os nipes da cartas
            é guardado a numeração das cartas em uma lista
            é criada uma variavel weight para guarda o peso das cartas
            e feito um for para que cada interação é chamado o objeto carta com as características das cartas
            e guardado em uma lista de baralhos
            o baralho é embaralhado
            e feito outro for para adicionar todas as cartas na pilha

        """
        self.reset_baralho()
        naipe = ["Ouro", "Espada", "Paus", "Copas"]
        numeracao = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "valete", "dama", "rei"]
        weight = 1
        baralho = list()
        for idx in range(len(naipe)):
            for id in numeracao:
                baralho.append(Carta(naipe[idx], id, weight))
                weight += 1

            weight = 1

        shuffle(baralho)
        for card in baralho:
            self.add_card(card)
