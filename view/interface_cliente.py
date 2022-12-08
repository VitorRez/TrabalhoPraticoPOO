from interface import *
from tkinter import *
from cliente_add import *
from tabela_cliente import *
import sys
sys.path.insert(0, '/home/vitor/Documentos/POO/trabalho prático/')
from vetorCliente import *
from persistencia_cliente import *
from cliente import *

class interface_cliente(interface):

    def __init__(self, nome, raiz, vc):
        super().__init__(nome, raiz)
        
        #Criei um frame e uma scrollbar nesse frmae
        self.frame = Frame(raiz)
        self.sb = Scrollbar(self.frame, orient=VERTICAL)
        
        self.vc = vc
        self.table = table(raiz, vc, self.frame, self.sb)
        self.table.table.pack(side=LEFT)
        
        #configurei a scrollbar
        self.sb.config(command=self.table.table.yview)
        self.sb.pack(side=RIGHT, fill=Y)
        self.frame.pack()
        
        self.bt1 = Button(raiz, text='Cadastrar Cliente', command=self.JanelaAdd)
        self.bt1.pack(side=LEFT)
        self.bt2 = Button(raiz, text='Fechar', command=self.fechar)
        self.bt2.pack(side=RIGHT)

    def JanelaAdd(self):
        raizAdd = Tk()
        interface_add_cliente(raizAdd, self.vc, self.table)
        raizAdd.mainloop()

    def fechar(self):
        self.raiz.destroy()

vc = VetorCliente()
pc = persistencia_cliente(vc)
pc.insercao(vc)
raiz = Tk()
interface_cliente('Clientes', raiz, vc)
raiz.mainloop()
pc.alteracao()

