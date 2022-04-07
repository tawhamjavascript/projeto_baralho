class Carta:
    def __init__(self, naipe: str, number: str, weight: int):
        self.__number = number
        self.__naipe = naipe
        self.__weight = weight
        self.__nextNode = None

    @property
    def naipe(self):
        return self.__naipe

    @property
    def numero(self):
        return self.__number

    @property
    def peso(self):
        return self.__weight

    def get_next_node(self):
        return self.__nextNode

    def set_next_node(self, next_node):
        self.__nextNode = next_node

    def has_next(self):
        return self.__nextNode is not None

    def __str__(self): # todas as informacoes da carta
        return f'{self.__number} de {self.__naipe}'

    def __eq__(self, other_object: 'Carta'):
        if self.peso == other_object.peso:
            return True

        return False

    def __gt__(self, other_object: 'Carta'):
        if self.peso > other_object.peso:
            return True

        return False




