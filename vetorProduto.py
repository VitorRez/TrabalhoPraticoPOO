#from entidade import Entidade
from Produto import Produto

class VetorProduto(Produto):
    def __init__(self):
        self.Produtos = []

    def addProduto(self, Produto):
        self.Produtos.append(Produto)
    
    def buscarProdutoNome(self, nome):
        for p in self.Produtos:
            if nome == p.nome:
                print("Produto encontrado\n")
                p.indentificacao()
                return p
        print("Produto não encontrado\n")
        return NONE

    def buscarProdutoCodigo(self, codigo):
        for p in self.Produtos:
            if codigo == p.codigo:
                print("Produto encotrado\n")
                p.indentificacao()
                return p
        print("Produto não encotrado\n")
        return NONE

    def listaProdutos(self):
        for p in self.Produtos:
            p.indentificacao()

    def venderProdutoCodigo(self, Produto, quantidadeVendida):
            p = buscarProdutoCodigo(Produto)
            p.quantidade = p.quantidade - quantidadeVendida

    def removerProdutoNome(self, Produto):
        p = buscarProdutoNome(Produto)
        p.quantidade = 0

    def removerProdutoCodigo(self, Produto):
        p = buscarProdutoCodigo(Produto)
        p.quantidade = 0