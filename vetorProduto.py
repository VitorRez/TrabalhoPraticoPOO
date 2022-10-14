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
            p = self.buscarProdutoCodigo(Produto)
            p.quantidade = p.quantidade - quantidadeVendida

    def removerProdutoCodigo(self, Produto):
        p = buscarProdutoCodigo(Produto)
        p.identificacao()
        x = int(input("\nVocê realmente deeja excluir esse item? \n digite: \n1- Sim \n2- Não"))
        if x==1:
            self.Produtos.remove(p)
        elif x==2:
            return

    def adicionarProdutoNome(self, Produto, Qtd):
        p = buscarProdutoNome(Produto)
        p.quantidade = p.quantiade + Qtd

    def adicionarProdutoCodigo(self, Produto, Qtd):
        p = buscarProdutoCodigo(Produto)
        p.quantidade = p.quantiade + Qtd