from abc import ABC, abstractmethod

class Entidade (ABC):

    def __init__(self, id):
        self.id = id

    @abstractmethod
    def identificacao(self): pass


