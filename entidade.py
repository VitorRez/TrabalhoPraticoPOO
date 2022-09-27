from abc import ABC, abstractmethod

class Entidade (ABC):

    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    @abstractmethod
    def identificacao(self): pass


