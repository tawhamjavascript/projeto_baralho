from random import shuffle
from Carta import Carta
from BaralhoException import BaralhoException


class BaralhoMontado:
    def __init__(self):
        self.__baralho = list()
        naipe = ["Ouro", "Espada", "Paus", "Copas"]
        numeracao = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "valete", "dama", "rei"]
        weight = 1

        for idx in range(len(naipe)):
            for id in numeracao:
                self.__baralho.append(Carta(naipe[idx], id, weight))
                weight += 1

            weight = 1

    def __len__(self):
        return len(self.__baralho)

    def temCarta(self):
        if len(self.__baralho) > 0:
            return True
        else:
            return False

    def retirarCarta(self):
        try:
            return self.__baralho.pop()
        except IndexError:
            raise BaralhoException('O baralho está vazio. Não há cartas para retirar')

    def embaralhar(self):
        shuffle(self.__baralho)

    def __str__(self):
        saida = ''
        for carta in self.__baralho:
            saida += carta.__str__() + '\n'

        return saida
