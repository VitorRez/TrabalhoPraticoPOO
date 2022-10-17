from entidade import Entidade

class produto(Entidade):
    def __init__(self, nome, codigo, precounitario, quantidade):
        super().__init__(codigo, nome)
        self.quantidade = quantidade
        self.preco_unitario = precounitario

    def retorna_nome(self):
        return self.nome

    def retorna_codigo(self):
        return self.id

    def retorna_quantidade(self):
        return self.quantidade

    def retorna_precounitario(self):
        return self.precounitario

    def identificacao(self):
        print("Nome: ", self.nome, "Código: ", self.id, "Preço unitário: ", self.preco_unitario, "Quantidade: ", self.quantidade)