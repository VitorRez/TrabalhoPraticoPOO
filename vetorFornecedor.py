#from entidade import Entidade
from Fornecedores import Fornecedor
from Produto import produto

class vetorFornecedor:
    def __init__(self):
        self.Fornecedores = []

    def addFornecedor(self, Fornecedor):
        self.Fornecedores.append(Fornecedor)

    def buscarFornecedorNome(self, nome):
        for f in self.Fornecedores:
            if nome == f.nome:
                print("Fornecedor encontrado\n")
                f.identificacao()
                return f
        print("Fornecedor não encontrado\n")
        return None

    def listaFornecedores(self):
            for f in self.Fornecedores:
                f.identificacao()

    def buscarFornecedorCnpj(self, cnpj):
        for f in self.Fornecedores:
            if cnpj == f.id:
                print("Fornecedor encontrado\n")
                f.identificacao()
                return f
        print("Fornecedor não encontrado\n")
        return None

    def removerFornecedorCnpj(self, cnpj):
        f = self.buscarFornecedorCnpj(cnpj)
        if f != None:
            self.Fornecedores.remove(f)
        else:
            return
