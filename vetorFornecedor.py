#from entidade import Entidade
from Fornecedores import Fornecedor
from Produto import Produto

class vetorFornecedor(Fornecedor):
    def __init__(self):
        self.Fornecedores = []

    def addFornecedor(self, Fornecedor):
        self.Fornecedores.append(Fornecedor)

    def buscarFornecedorNome(self, nome):
        for f in self.Fornecedores:
            if nome == f.nome:
                print("Produto encontrado\n")
                f.indentificacao()
                return f
        print("Produto não encontrado\n")
        return NONE

    def listaFornecedores(self):
            for f in self.Fornecedores:
                f.indentificacao()

    def buscarFornecedorCnpj(self, cnpj):
        for f in self.Fornecedores:
            if cnpj == f.cnpj:
                print("Produto encontrado\n")
                f.indentificacao()
                return f
        print("Produto não encontrado\n")
        return NONE

    def removerFornecedorCnpj(self, cnpj):
        f = buscarFornecedorCodigo(cnpj)
        self.Fornecedores.remove(f)
