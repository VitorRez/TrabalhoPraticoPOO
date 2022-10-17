from entidade import Entidade

class Fornecedor(Entidade):
    def __init__(self, nome, cnpj, telefone, endereco):
        super().__init__(cnpj, nome)
        self.telefone = telefone
        self.endereco = endereco

    def retorna_nome(self):
            return self.nome

    def retorna_cnpj(self):
            return self.id

    def retorna_telefone(self):
            return self.telefone
        
    def retorna_endereco(self):
            return self.endereco

    def identificacao(self):
            print("Nome: ", self.nome, "cnpj: ", self.id, "Telefone: ", self.telefone, "Endereço: ", self.endereco)