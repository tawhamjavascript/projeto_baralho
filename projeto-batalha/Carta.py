class Carta:
    def __init__(self, naipe: str, number: str, weight: int):
        self.__number = number  # guards a numeração da carta
        self.__naipe = naipe    # guarda o naipe da carta
        self.__weight = weight  # guarda o peso da carta
        self.__nextNode = None  # guarda o próximo nó

    @property
    def naipe(self):  # retorna o nipe da carta
        return self.__naipe

    @property
    def numero(self):  # retorna a númeração da carta
        return self.__number

    @property
    def peso(self):  # retorna o peso da carta
        return self.__weight

    def get_next_node(self):  # retorna o próximo Nó
        return self.__nextNode

    def set_next_node(self, next_node):  # configura o nó atual, para apontar para o próximo Nó
        self.__nextNode = next_node

    def has_next(self):  # verifica se o nó aponta para o nullo
        return self.__nextNode is not None

    def __str__(self):  # todas as informacoes da carta
        return f'{self.__number} de {self.__naipe}'

    def __eq__(self, other_object: 'Carta'):
        # método especial de python responsável por verificar se dois objetos são iguais
        if self.peso == other_object.peso:
            return True

        return False

    def __gt__(self, other_object: 'Carta'):
        # método especial de python responsável por verificar se um objeto é maior que o outro
        if self.peso > other_object.peso:
            return True

        return False
