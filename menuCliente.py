from cliente import Cliente
from vetorCliente import VetorCliente

class Menu:
  def menu():
    x = int(input("Digite: \n0 para sair\n1 para cadastrar do cliente\n2 para buscar o cliente\n"))

    while x != 0:
      if x == 1:
        nome = input("Digite o nome do cliente: ")
        tel = input("Digite o telefone do cliente: ")
        end = input("Digite o endereço do cliente: ")
        cpf = input("Digite o cpf do cliente: ")
        VetorCliente.addCliente(Cliente(nome, tel, end, cpf))#Ta dando erro aqui
      elif x == 2:
        x = int(input("Digite 1 se quiser buscar pelo nome, ou 2 se quiser buscar pelo cpf"))
        while x != 1 and x != 2:
          print("Digite um valor válido\n")
          x = int(input("Digite 1 se quiser buscar pelo nome, ou 2 se quiser buscar pelo cpf"))

        if x == 1:
          nome = input("Digite o nome do cliente")
          c = VetorCliente.buscaClienteNome(nome)
        elif x == 2:
          cpf = input("Digite o cpf do cliente")
          c = VetorCliente.buscaClienteCpf(cpf)

      x = int(input("Digite: \n0 para sair\n1 para cadastrar do cliente\n2 para buscar o cliente\n"))
