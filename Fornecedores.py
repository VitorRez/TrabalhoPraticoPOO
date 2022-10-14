from entidade import Entidade

class Fornecedor(Entidade):
    def __init__(self, nome, cnpj, telefone, endereco):
        super().__init__(nome, cnpj)
        self.telefone = telefone
        self.endereco = endereco
        self.codigo = cnpj

        def retorna_nome(self):
            return self.nome

        def retorna_cnpj(self):
            return self.cnpj

        def retorna_telefone(self):
            return telefone
        
        def retorna_endereco(self):
            return endereco

        def identificacao(self):
            print(self.nome, self.cnpj, self.telefone, self.endereco)