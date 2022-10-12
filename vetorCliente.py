#from entidade import Entidade
from cliente import Cliente

class VetorCliente(Cliente):
  def __init__(self):
    self.clientes = []

  def addCliente(self, cliente):
    self.clientes.append(cliente)

  def buscaClienteNome(self, nome):
    for c in self.clientes:
      if nome == c.nome:
        print("Cliente encontrado\n")
        c.identificacao()
        return
    print("Cliente não encontrado\n")
    return

  def buscaClienteCpf(self, cpf):
    for c in self.clientes:
      if cpf == c.id:
        print("Cliente encontrado\n")
        c.identificacao()
        return
    print("Cliente não encontrado\n")
    return

  def listaClientes(self):
    for c in self.clientes:
      c.identificacao()
