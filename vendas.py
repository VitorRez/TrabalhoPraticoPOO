from cliente import Cliente
#from produto import produto
from entidade import Entidade

class Venda(Entidade):
    def __init__ (self, Quantidade = 0, Total = 0, IdProduto = 0):
        super().__init__("venda", IdProduto)
        self.Quantidade = Quantidade
        self.Total = Total

    def Qtd_Prod(self, Quantidade):
        self.Quantidade = Quantidade

    def Total_Valor(self, Total):
        self.Total = Total
            
    def Codigo(self, IdProduto):
        self.IdProduto = IdProduto

    def retorna_Codigo(self):
        return self.IdProduto
            
    def retorna_Quantidade(self):
        return self.Quantidade

    def retorna_Total(self):
        return self.Total
    
    def identificacao(self):
        print(self.nome, self.id, self.Quantidade, self.Total)