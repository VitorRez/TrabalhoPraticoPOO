from tkinter import *
from tkinter import ttk

class table:

    def __init__(self, raiz, vetor, frame, sb):
        self.raiz = raiz
        self.table = Listbox(frame, width=80, yscrollcommand=sb.set)#coloquei a listbox no frame e n na janela e dei o comando da scrollbar
        self.table.insert(END, 'Nome                CPF                 Telefone            Endereço            ')
        for i in vetor.clientes:
            self.preenche(i)
        self.table.pack()

    def preenche(self, i):
        nome = str(i.nome)
        cpf = str(i.id)
        telefone = str(i.telefone)
        endereco = str(i.endereco)
        text = nome.ljust(20, ' ') + cpf.ljust(20, ' ') + telefone.ljust(20, ' ') + endereco.ljust(20, ' ')
        self.table.insert(END, text)
        self.table.config(font='TkFixedFont')

    def fecha(self):
        self.raiz.destroy()
