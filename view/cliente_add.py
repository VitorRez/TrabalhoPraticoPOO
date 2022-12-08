from tkinter import *
import sys
sys.path.insert(0, '/home/vitor/Documentos/POO/trabalho prático/')
from vetorCliente import *
from persistencia_cliente import *
from cliente import *

class interface_add_cliente():

    def __init__(self, raiz, vc, t):
        self.table = t
        self.vc = vc
        self.raiz = raiz
        self.raiz.title("Adicionar Fornecedor")
        Label(self.raiz, text='Nome').grid(row=1, column=1, sticky=W, pady=5)
        Label(self.raiz, text='Cpf').grid(row=2, column=1, sticky=W, pady=5)
        Label(self.raiz, text='Telefone').grid(row=3, column=1, sticky=W, pady=5)
        Label(self.raiz, text='Endereço').grid(row=4, column=1, sticky=W, pady=5)
        self.nome=Entry(self.raiz, width=10)
        self.nome.grid(row=1, column=2, sticky=E+W, pady=5, padx=5)
        self.id=Entry(self.raiz, width=10)
        self.id.grid(row=2, column=2, sticky=E+W, pady=5, padx=5)
        self.telefone=Entry(self.raiz, width=10)
        self.telefone.grid(row=3, column=2, sticky=E+W, pady=5, padx=5)
        self.endereco=Entry(self.raiz, width=10)
        self.endereco.grid(row=4, column=2, sticky=E+W, pady=5, padx=5)
        self.bt1 = Button(raiz, text = 'Adicionar', command=self.adiciona)
        self.bt1.grid(row=5, column=1, sticky=E+W, pady=5, padx=5)
        self.bt2 = Button(raiz, text = 'Fechar', command=self.fechar)
        self.bt2.grid(row=5, column=2, sticky=E+W, pady=5, padx=5)
        vc = self.vc

    def fechar(self):
        self.raiz.destroy()

    def adiciona(self):
        cliente = Cliente(self.nome.get(), self.id.get(), self.telefone.get(), self.endereco.get())
        self.vc.addCliente(cliente)
        self.table.preenche(cliente)
        #self.f = [self.nome.get(), self.id.get(), self.telefone.get(), self.endereco.get()]
        print(self.nome.get(), self.id.get(), self.telefone.get(), self.endereco.get())
        self.raiz.destroy()