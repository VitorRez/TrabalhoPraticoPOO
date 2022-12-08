from tkinter import *
import sys
sys.path.insert(0, '/home/vitor/Documentos/POO/trabalho prático/')
from vetorFornecedor import *
from persistencia_fornecedores import *
from Fornecedores import *

class interface_add_fornecedor():

    def __init__(self, raiz, vf, t):
        self.table = t
        self.vf = vf
        self.raiz = raiz
        self.raiz.title("Adicionar Fornecedor")
        Label(self.raiz, text='Nome').grid(row=1, column=1, sticky=W, pady=5)
        Label(self.raiz, text='Cnpj').grid(row=2, column=1, sticky=W, pady=5)
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
        vf = self.vf

    def fechar(self):
        self.raiz.destroy()

    def adiciona(self):
        fornecedor = Fornecedor(self.nome.get(), self.id.get(), self.telefone.get(), self.endereco.get())
        self.vf.addFornecedor(fornecedor)
        self.table.preenche(fornecedor)
        #self.f = [self.nome.get(), self.id.get(), self.telefone.get(), self.endereco.get()]
        print(self.nome.get(), self.id.get(), self.telefone.get(), self.endereco.get())
        
        #limpa os campos de entrada de dados para add mais
        self.nome.delete(0, END)
        self.id.delete(0, END)
        self.telefone.delete(0, END)
        self.endereco.delete(0, END)
        
        #self.raiz.destroy()


