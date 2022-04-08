from random import shuffle
from Carta import Carta
from BaralhoException import BaralhoException


class BaralhoMontado:
    def __init__(self):
        self.__baralho = list()
        naipe = ["Ouro", "Espada", "Paus", "Copas"]  # salva os tipos de cartas
        numeracao = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "valete", "dama", "rei"]  #guarda a numeração das cartas
        weight = 1  # guarda o peso das cartas

        for idx in range(len(naipe)): # responsável por montar o baralho e guardar o baralho na classe carta
            for id in numeracao:
                self.__baralho.append(Carta(naipe[idx], id, weight))
                weight += 1

            weight = 1

    def __len__(self): # retorna o tamanho do baralho
        return len(self.__baralho)

    def temCarta(self): # verifica se o baralho tem carta ou não
        if len(self.__baralho) > 0:
            return True

        else:
            return False

    def retirarCarta(self):
        # Se o baralho tiver carta é chamado o método de array pop
        # se não tiver é levantado a excessão IndexError, propagando o erro BaralhoException
        try:
            return self.__baralho.pop()

        except IndexError:
            raise BaralhoException('O baralho está vazio. Não há cartas para retirar')

    def embaralhar(self):
        # chama o método da biblioteca random responsável por embaralhar arrays
        shuffle(self.__baralho)

    def __str__(self):
        # retorna todos os dados do baralho
        saida = ''
        for carta in self.__baralho:
            saida += carta.__str__() + '\n'

        return saida
