from PilhaException import PilhaException
from Carta import Carta


class Pilha:
    def __init__(self):
        self.__head = None  # guarda a referência de memória da carta do topo do deck
        self.__length = 0   # guarda o tamanho do deck do jogador
        self.__base = None  # guarda a referência de memória da última carta do deck

    def length_deck(self):  # retorna o tamanho
        return self.__length

    def stack_up(self, value: Carta):
        # Verifica se o topo do deck é nullo
        # se não a nova carta vai apontar para o nulo
        # vai ser atualizada a variável que aponta para a base do deck
        # se for nulo a nova carta vai apontar para o topo atual
        # após essas checagens o topo será a nova carta recebida
        # e a quantidade de cartas é atualizada
        newHead = value
        if self.__head is None:
            self.__base = newHead

        newHead.set_next_node(self.__head)
        self.__head = newHead
        self.__length += 1

    def unstack(self):  # retorna a carta do topo do deck
        # faz um if para verificar se o deck está vazio
        # se não estiver o novo topo do deck será a próxima carta do deck
        # A quantidade de carta é subtraída em - 1
        # é retornado o antigo topo
        # se o deck estiver vazio é levantado uma excessão do tipo pilha exception
        if not self.is_empty():
            oldHead = self.__head
            self.__head = oldHead.get_next_node()
            self.__length -= 1
            return oldHead

        raise PilhaException("Pilha está vazia")

    def reset_stack(self):  # Responsável por zerar o deck do utilizador
        self.__head = None
        self.__base = None
        self.__length = 0

    def stack_base(self, value: Carta):  # atualiza a base do deck com a carta recebida
        # Quando a nova carta é recebida, a mesma é configurada para apontar para o null
        # é colocado que a base atual vai apontar a nova carta, atualizando assim a base
        # O tamanho do deck é incrementado
        newBase = value
        newBase.set_next_node(None)
        if self.__head is None:
            self.__head = self.__base = newBase

        else:
            self.__base.set_next_node(newBase)
            self.__base = newBase

        self.__length += 1

    def is_empty(self):  # verifica se o topo do deck é vazio
        return self.__head is None

    def elements_in_stack(self):  # chama o método __str__
        self.__str__()

    def elemento(self, posicao):
        # Pecorre os nós até a posição informada seja igual à posição do nó correspondente
        # caso isso ocorra é retornado os dados do Nó
        # se a posição não for um inteiro é levantada uma exceção
        # se a posição informada não corresponder a nenhum nó é levantada uma exceção
        try:
            assert 0 < posicao <= self.__length
            cursor = self.__head
            count = 1
            while cursor is not None and count < posicao:
                count += 1
                cursor = cursor.prox

            return str(cursor)

        except TypeError:
            raise PilhaException('Digite um número inteiro referente ao elemento desejado')
        except AssertionError:
            raise PilhaException(f'O elemento {posicao} NAO existe na pilha de tamanho {self.__length}')
        except:
            raise

    def find(self, valor):
        # pecorre os nós até que o valor informado seja igual aos dados de um nó
        # quando isso ocorre é retornado a posição do nó
        # caso não exista esse valor nos Nós é levantada uma excessão
        cursor = self.__head
        count = 1
        while cursor is not None:
            if str(cursor) == valor:
                return count

            cursor = cursor.prox
            count += 1

        raise PilhaException(f'Valor {valor} nao esta na pilha', 'busca()')

    def __str__(self):  # Pecorre todos os nós do deck exibindo os seus determinados valores
        head = self.__head
        string = "topo -> ["
        first = True
        while head is not None:
            if first:
                string += f"{ str(head) }"
                first = False

            else:
                string += f", { str(head) }"

            head = head.get_next_node()

        string += ']'
