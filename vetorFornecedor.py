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
        x = int(input("Fornecedor não encontrado, deseja cadastrar o fornecedor?\nSim: 1\nNão: 2\n"))
        if x == 1:
            fcnpj = int(input("Digite o cnpj do fornecedor: "))
            fend = input("Digite o endereço do fornecedor: ")
            ftel = input("Digite o telefone do fornecedor: ")
            f = Fornecedor(nome, fcnpj, ftel, fend)
            self.addFornecedor(f)
        if x == 2:
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
        x = int(input("Fornecedor não encontrado, deseja cadastrar o fornecedor?\nSim: 1\nNão: 2\n"))
        if x == 1:
            fnome = input("Digite o nome do fornecedor: ")
            fend = input("Digite o endereço do fornecedor: ")
            ftel = input("Digite o telefone do fornecedor: ")
            f = Fornecedor(fnome, cnpj, ftel, fend)
            self.addFornecedor(f)
        if x == 2:
            return None

    def removerFornecedorCnpj(self, cnpj):
        f = self.buscarFornecedorCnpj(cnpj)
        if f != None:
            self.Fornecedores.remove(f)
        else:
            return
