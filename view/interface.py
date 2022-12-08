from tkinter import *
from abc import ABC, abstractmethod

class interface (ABC):

    def __init__(self, nome, raiz):
        self.raiz = raiz
        self.raiz.title(nome)

    @abstractmethod
    def fechar(): pass