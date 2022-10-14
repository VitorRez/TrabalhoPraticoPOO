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
        return c
    x = int(input("Cliente não encontrado, deseja cadastrar o cliente?\n1 sim\n2 não\n"))
    if x == 1:
       ctel = input("Digite o telefone do cliente: ")
       cend = input("Digite o endereço do cliente: ")
       ccpf = input("Digite o cpf do cliente: ")
       c = Cliente(nome, ctel, cend, ccpf)
       self.addCliente(c)
       return c
    if x == 2:
      return

  def buscaClienteCpf(self, cpf):
    for c in self.clientes:
      if cpf == c.id:
        print("Cliente encontrado\n")
        c.identificacao()
        return c
    x = int(input("Cliente não encontrado, deseja cadastrar o cliente?\n1 sim\n2 não\n"))
    if x == 1:
       cnome = input("Digite o nome do cliente: ")
       ctel = input("Digite o telefone do cliente: ")
       cend = input("Digite o endereço do cliente: ")
       c = Cliente(cnome, ctel, cend, cpf)
       self.addCliente(c)
       return c
    if x == 2:
      return

  def listaClientes(self):
    for c in self.clientes:
      c.identificacao()
