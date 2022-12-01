from entidade import Entidade
from cliente import *
from Produto import *
from vetorProduto import *
from vetorCliente import *

class Venda(Entidade):
    def __init__ (self, cliente, codigo):
        super().__init__(codigo)
        self.cliente = cliente
        self.carrinho = []

    def identificacao(self):
        for p in self.carrinho:
            print(p.nome, p.quantidade)

    def addCarrinhoCodigo(self, quantidade, vp, codigo):
        p = vp.buscarProdutoCodigo(codigo)
        if p == None:
            return 1
        if p.quantidade < quantidade:
            return 2
        p2 = produto(p.nome, p.id, p.fornecedor, p.preco_unitario, quantidade)
        p.quantidade -= quantidade
        self.carrinho.append(p2)
        return 0

    def addCarrinhoNome(self, quantidade, vp, nome):
        p = vp.buscarProdutoNome(nome)
        if p == None:
            return 1
        if p.quantidade < quantidade:
            return 2
        p2 = produto(p.nome, p.id, p.fornecedor, p.preco_unitario, quantidade)
        p.quantidade -= quantidade
        self.carrinho.append(p2)
        return 0

    def removeCarrinho(self, codigo):
        for p in self.carrinho:
            if p.id == codigo:
                self.carrinho.remove(p)
                return
    
    def alteraQntdCodigo(self, codigo, vp, quantidade):
        produto = vp.buscarProdutoCodigo(codigo)
        if produto == None:
            return
        for p in self.carrinho:
            if p.id == produto.id:
                if p.quantidade > quantidade:
                    vp.adicionarProdutoCodigo(produto.id, quantidade)
                else:
                    vp.adicionarProdutoCodigo(produto.id, quantidade - produto.quantidade)
                p.quantidade = quantidade

    def alteraQntdNome(self, nome, vp, quantidade):
        produto = vp.buscarProdutoNome(nome)
        if produto == None:
            return
        for p in self.carrinho:
            if p.id == produto.id:
                if p.quantidade > quantidade:
                    vp.adicionarProdutoCodigo(produto.id, quantidade)
                else:
                    vp.adicionarProdutoCodigo(produto.id, quantidade - produto.quantidade)
                p.quantidade = quantidade

    def finalizarVenda(self):
        valor_total = 0
        for p in self.carrinho:
            valor_total += p.quantidade * p.preco_unitario
            print("Item: ", p.nome)
            print("Quantidade: ", p.quantidade)
            print("Valor unitário: ", p.preco_unitario)
        print("\nTotal da compra: ", valor_total)

    def listaCarrinho(self):
        for p in self.carrinho:
            print(p.nome)
            print(p.fornecedor.nome)

    def cancelarVenda(self, vp):
        for p in self.carrinho:
            p1 = vp.buscarProdutoCodigo(p.id)
            p1.quantidade += p.quantidade
        self.carrinho.clear()
