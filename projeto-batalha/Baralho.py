from Carta import Carta
from PilhaException import PilhaException
from random import shuffle
from BaralhoException import BaralhoException
from BaralhoMontado import BaralhoMontado


class Baralho:
    def __init__(self):
        self.__head = None
        self.__length = 0
        self.__baralhoMontado = BaralhoMontado()
        self.__baralhoMontado.embaralhar()

        while self.__baralhoMontado.temCarta():
            card = self.__baralhoMontado.retirarCarta()
            self.stack_up(card)

    def stack_up(self, card):
        newHead = card
        newHead.set_next_node(self.__head)

        self.__head = newHead
        self.__length += 1

    def unstack(self):
        if not self.is_empty():
            data = self.__head
            self.__head = self.__head.get_next_node()
            self.__length -= 1
            return data

        raise PilhaException('A pilha está vazia')

    def __len__(self) -> int:
        return self.__length

    def elem_of_stack(self):
        print(self.__str__())

  
    def find_value(self, value):
        node = self.__head
        count = 1
        while node is not None:
            if str(node) == value:
                return count

            node = node.get_next_node()
            count += 1

        raise PilhaException(f'Valor {value} não esta na pilha', 'busca()')

    def position_of_element(self, position):
        try:
            assert position > 0 and position <= self.__len__
            node = self.__head
            count = 1
            while node is not None and count < position:
                count += 1
                node = node.get_next_node()

            return str(node)

        except TypeError:
            raise PilhaException('Digite um número inteiro referente ao elemento desejado')
        except AssertionError:
            raise PilhaException(f'O elemento {position} NAO existe na pilha de tamanho {self.__length}')
        except:
            raise

    def is_empty(self) -> bool:
        return self.__head is None

    def __str__(self):
        node = self.__head
        first = True
        string = "topo --> ["
        while node is not None:
            if first:
                string += f"{str(node)}"
                first = False

            else:
                string += f", {str(node)}"

            node = node.get_next_node()

        string += "]"
        return string





if __name__ == "__main__":
    baralho = Baralho()
    count = 0
    """while True:
       try:
            print(baralho.unstack())
            count += 1
            print(count)

       except PilhaException as error:
           print(error)
           break"""
    
    print(baralho.position_of_element(5))
