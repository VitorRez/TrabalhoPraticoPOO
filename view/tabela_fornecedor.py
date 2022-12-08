from tkinter import *
from tkinter import ttk




class table:

    def __init__(self, raiz, vetor):
        self.raiz = raiz
        self.table = Listbox(raiz, width=80)
        self.table.insert(END, 'Nome                CNPJ                Telefone            Endereço            ')
        for i in vetor.Fornecedores:
            self.preenche(i)
        self.table.pack()

    def preenche(self, i):
        nome = str(i.nome)
        cnpj = str(i.id)
        telefone = str(i.telefone)
        endereco = str(i.endereco)
        text = nome.ljust(20, ' ') + cnpj.ljust(20, ' ') + telefone.ljust(20, ' ') + endereco.ljust(20, ' ')
        self.table.insert(END, text)
        self.table.config(font='TkFixedFont')

    def fecha(self):
        self.raiz.destroy()
        
            