from abc import ABC, abstractmethod

class persistencia (ABC):
    
    def __init__(self, v):
        self.vetor = v

    @abstractmethod
    def insercao() : pass
    def alteracao() : pass
    def exclusao() : pass