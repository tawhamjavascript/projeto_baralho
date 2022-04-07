from Carta import Carta
from PilhaException import PilhaException

class Jogador:
    def __init__(self, name: str):
        self.__name = name
        self.__head = None
        self.__length = 0
        self.__score = 0
        self.__base = None

    @property
    def nome(self):
        return self.__name

    @property
    def pontuacao(self):
        return self.__score

    @property
    def tamanho(self):
        return self.__length

    def stack_up(self, value: Carta):
        newHead = value
        if self.__head is None:
            newHead.set_next_node(None)
            self.__base = newHead

        else:
            newHead.set_next_node(self.__head)

        self.__length += 1
        self.__head = newHead
        self.__score += newHead.peso

    def unstack(self):
        if not self.is_empty():
            oldHead = self.__head
            self.__head = oldHead.get_next_node()
            self.__score -= oldHead.peso
            self.__length -= 1
            return oldHead

        raise PilhaException("Pilha está vazia")

    def stack_base(self, value: Carta):
        newBase = value
        newBase.set_next_node(None)
        self.__base.set_next_node(newBase)
        self.__score += newBase.peso
        self.__base = newBase
        self.__length += 1

    def is_empty(self):
        return self.__length == 0

    def elem_in_stack(self):
        head = self.__head
        while head is not None:
            print(str(head))
            head = head.get_next_node()

    def __str__(self):
        return f"Jogador {self.__name}, tem {self.__length} cartas e sua pontuação é {self.__score}"


if __name__ == "__main__":
    jogador = Jogador("nada")
    jogador.stack_up(Carta("verme", "10", 10))
    jogador.stack_up_base(Carta("azul", "20", 5))
    jogador.unstack()
    jogador.elem_in_stack()
    print(jogador.pontuacao)
    jogador.unstack()
    print(jogador.pontuacao)
    jogador.unstack()








