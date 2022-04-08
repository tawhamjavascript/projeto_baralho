from PilhaException import PilhaException
from BaralhoMontado import BaralhoMontado


class Baralho:
    def __init__(self):
        self.__head = None  # guarda o topo da pilha
        self.__length = 0   # indica o tamanho da pilha
        self.__baralhoMontado = BaralhoMontado()  # cria uma instância de um objeto
        self.__baralhoMontado.embaralhar() # chama o método embaralhar do objeto

        while self.__baralhoMontado.temCarta():
            # A cara interação é verificado se tem carta
            # se tiver é retirado a carta e chamada a função stack_up
            # se não tiver mais cartas a interação é parada
            card = self.__baralhoMontado.retirarCarta()
            self.stack_up(card)

    def stack_up(self, card):
        # topo será atualizado para a nova carta recebida
        # e a quantidade de cartas é atualizada
        newHead = card
        newHead.set_next_node(self.__head)
        self.__head = newHead
        self.__length += 1

    def unstack(self):
        # faz um if para verificar se o deck está vazio
        # se não estiver o novo topo do deck será a próxima carta do deck
        # A quantidade de carta é subtraída em - 1
        # E é retornado o antigo topo
        # se o deck estiver vazio é levantado uma excessão do tipo pilha exception
        if not self.is_empty():
            data = self.__head
            self.__head = self.__head.get_next_node()
            self.__length -= 1
            return data

        raise PilhaException('A pilha está vazia')

    def __len__(self) -> int: # retorna o tamanho do baralho
        return self.__length

    def element_of_stack(self): # retorna os dados fornecidos pelo método __str__
        return self.__str__()

    def find_value(self, value):
        # pecorre os nós até que o valor informado seja igual aos dados de um nó
        # quando isso ocorre é retornado a posição do nó
        # caso não exista esse valor nos Nós é levantada uma excessão
        node = self.__head
        count = 1
        while node is not None:
            if str(node) == value:
                return count

            node = node.get_next_node()
            count += 1

        raise PilhaException(f'Valor {value} não esta na pilha', 'busca()')

    def position_of_element(self, position):
        # Pecorre os nós até a posição informada seja igual a posição do nó correspondente
        # caso isso ocorra é retornado os dados do Nó
        # se a posição não for um inteiro é levantada uma exceção
        # se a posição informada não corresponder a nenhum nó é levantada uma exceção
        try:
            assert 0 < position <= self.__length
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

    def is_empty(self) -> bool:  # verifica se o topo do baralho está vazio
        return self.__head is None

    def __str__(self):  # Pecorre todos os nós do baralho exibindo os seus determinados valores
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
