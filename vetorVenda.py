from vetorProduto import *
from cliente import *
from Produto import *
from vetorCliente import *
from entidade import *
from persistencia import *
from novaVenda import Venda

class vetorVenda(Venda):
    def __init__(self):
        self.vendas = []

    def addVenda(self, venda):
        self.vendas.append(venda)

    def listaVendas(self):
        for v in self.vendas:
            print(v.cliente.nome)
            print(v.cliente.id)
            for c in v.carrinho:
                print(c.nome)
                print(c.preco_unitario)
                print(c.quantidade)
    