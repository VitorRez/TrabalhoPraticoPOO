#from entidade import Entidade
from Produto import produto

class VetorProduto(produto):
    def __init__(self):
        self.Produtos = []

    def addProduto(self, Produto):
        for p in self.Produtos:
            if p.nome == Produto.nome or p.codigo == Produto.codigo:
                x = int(input("Produto ja cadastrado, deseja adicionar a quantidade registrada?\n1 sim\n2 não "))
                if x == 1:
                    p.quantidade += Produto.quantidade
                    return
                if x == 2:
                    return
        self.Produtos.append(Produto)
        
    
    def buscarProdutoNome(self, nome):
        for p in self.Produtos:
            if nome == p.nome:
                print("Produto encontrado")
                p.identificacao()
                return p
        print("Produto não encontrado")
        return None

    def buscarProdutoCodigo(self, codigo):
        for p in self.Produtos:
            if codigo == p.codigo:
                print("Produto encotrado")
                p.identificacao()
                return p
        print("Produto não encotrado")
        return None

    def listaProdutos(self):
        for p in self.Produtos:
            p.identificacao()

    def venderProdutoCodigo(self, Produto, quantidadeVendida):
            p = self.buscarProdutoCodigo(Produto.codigo)
            p.quantidade = p.quantidade - quantidadeVendida

    def removerProdutoNome(self, Produto):
        p = self.buscarProdutoNome(Produto)
        p.quantidade = 0

    def removerProdutoCodigo(self, Produto):
        p = self.buscarProdutoCodigo(Produto)
        p.quantidade = 0