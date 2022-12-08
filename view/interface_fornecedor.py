from interface import *
from tkinter import *
from fornecedor_add import *
from tabela_fornecedor import *
import sys
sys.path.insert(0, '/home/vitor/Documentos/POO/trabalho prático/')
from vetorFornecedor import *
from persistencia_fornecedores import *
from Fornecedores import *

class interface_fornecedor(interface):

    def __init__(self, nome, raiz, vf):
        super().__init__(nome, raiz)
        
        #Criei um frame e uma scrollbar nesse frmae
        self.frame = Frame(raiz)
        self.sb = Scrollbar(self.frame, orient=VERTICAL)
        
        self.vf = vf
        self.table = table(raiz, vf, self.frame, self.sb)
        self.table.table.pack(side=LEFT)
        
        #configurei a scrollbar
        self.sb.config(command=self.table.table.yview)
        self.sb.pack(side=RIGHT, fill=Y)
        self.frame.pack()
        
        self.bt1 = Button(raiz, text='Cadastrar Fornecedor', command=self.JanelaAdd)
        self.bt1.pack(side=LEFT)
        self.bt2 = Button(raiz, text='Fechar', command=self.fechar)
        self.bt2.pack(side=RIGHT)

    def JanelaAdd(self):
        raizAdd = Tk()
        f = []
        interface_add_fornecedor(raizAdd, self.vf, self.table)
        raizAdd.mainloop()

    def fechar(self):
        self.raiz.destroy()

vf = vetorFornecedor()
pf = persistencia_fornecedor(vf)
pf.insercao(vf)
raiz = Tk()
interface_fornecedor('Fornecedores', raiz, vf)
raiz.mainloop()
pf.alteracao()
