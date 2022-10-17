from cliente import Cliente
from vetorCliente import VetorCliente
from persistencia import Persistencia

class MenuCliente:
  def menuC(vc):
    x = int(input("Digite: \n0 Para sair\n1 Para cadastrar do cliente\n2 Para buscar o cliente\n"))
    while x != 0:
      if x == 1:
        nome = input("Digite o nome do cliente: ")
        nome = nome.title()
        tel = input("Digite o telefone do cliente: ")
        end = input("Digite o endereço do cliente: ")
        cpf = int(input("Digite o cpf do cliente: "))
        c = Cliente(nome, tel, end, cpf)
        vc.addCliente(c)
      elif x == 2:
        x = int(input("Digite: \n1 Se quiser buscar pelo nome\n2 Se quiser buscar pelo cpf\n3 Se quiser voltar\n"))
        while x != 1 and x != 2 and x != 3:
          print("Digite um valor válido\n")
          x = int(input("Digite: \n1 Se quiser buscar pelo nome\n2 Se quiser buscar pelo cpf\n3 Se quiser voltar\n"))

        if x == 1:
          nome = input("Digite o nome do cliente: ")
          nome = nome.title()
          c = vc.buscaClienteNome(nome)
          
        elif x == 2:
          cpf = input("Digite o cpf do cliente: ")
          c = vc.buscaClienteCpf(cpf)
          
          
      x = int(input("Digite: \n0 Para sair\n1 Para cadastrar do cliente\n2 Para buscar o cliente\n"))
