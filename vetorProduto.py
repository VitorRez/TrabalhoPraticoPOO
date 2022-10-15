#from entidade import Entidade
from Produto import produto

class VetorProduto(produto):
    def __init__(self):
        self.Produtos = []

    def addProduto(self, Produto):
        self.Produtos.append(Produto)
    
    def buscarProdutoNome(self, nome):
        for p in self.Produtos:
            if nome == p.nome:
                print("Produto encontrado\n")
                p.identificacao()
                return p
        print("Produto não encontrado\n")
        return None

    def buscarProdutoCodigo(self, codigo):
        for p in self.Produtos:
            if codigo == p.id:
                print("Produto encotrado\n")
                p.identificacao()
                return p
        print("Produto não encotrado\n")
        return None

    def listaProdutos(self):
        for p in self.Produtos:
            p.identificacao()

    def venderProdutoCodigo(self, Produto, quantidadeVendida):
            p = self.buscarProdutoCodigo(Produto)
            if p != None:
                p.quantidade = p.quantidade - quantidadeVendida
            else:
                return

    def removerProdutoCodigo(self, codigo):
        p = self.buscarProdutoCodigo(codigo)
        if p != None:
            x = int(input("\nVocê realmente deseja excluir esse item?\n1 Sim \n2 Não\n"))
            if x==1:
                self.Produtos.remove(p)
            elif x==2:
                return 
        else:
            return

    def adicionarProdutoNome(self, Produto, Qtd):
        p = self.buscarProdutoNome(Produto)
        if p != None:
            p.quantidade = p.quantidade + Qtd
        else:
            return

    def adicionarProdutoCodigo(self, Produto, Qtd):
        p = self.buscarProdutoCodigo(Produto)
        if p != None:
            p.quantidade = p.quantidade + Qtd
        else:
            return
