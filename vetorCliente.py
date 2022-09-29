#from entidade import Entidade
from cliente import Cliente

class VetorCliente(Cliente):
  def __init__(self):
    self.clientes = []

  def addCliente(self, cliente):
    self.clientes.append(cliente)

  def buscaClienteNome(self, nome):
    for c in self.clientes:
      if nome == c.nome:#vai dar erro aqui no futuro
        print("Cliente encontrado\n")
        return c
    print("Cliente não encontrado\n")
    return None

  def buscaClienteCpf(self, cpf):
    for c in self.clientes:
      if cpf == c.cpf:#e aqui tb, mas n sei como resolver
        print("Cliente encontrado\n")
        return c
    print("Cliente não encontrado\n")
    return None
