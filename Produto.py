from entidade import Entidade

class produto(Entidade):
    def __init__(self, nome, codigo, precounitario, quantidade):
        super().__init__(nome, codigo)
        self.nome = nome
        self.codigo = codigo
        self.quantidade = quantidade
        self.preco_unitario = precounitario

    def retorna_nome(self):
        return self.nome

    def retorna_codigo(self):
        return self.codigo

    def retorna_quantidade(self):
        return self.quantidade

    def retorna_precounitario(self):
        return self.precounitario

    def identificacao(self):
        print(self.nome, self.codigo, self.preco_unitario, self.quantidade)