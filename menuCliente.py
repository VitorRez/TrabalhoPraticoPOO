from cliente import Cliente
from vetorCliente import VetorCliente
from persistencia import Persistencia

class MenuCliente:
  def menuC(vc):
    x = int(input("Digite: \n0 para sair\n1 para cadastrar do cliente\n2 para buscar o cliente\n3 para voltar\n"))
    while x != 0:
      if x == 1:
        nome = input("Digite o nome do cliente: ")
        tel = input("Digite o telefone do cliente: ")
        end = input("Digite o endereço do cliente: ")
        cpf = input("Digite o cpf do cliente: ")
        c = Cliente(nome, tel, end, cpf)
        vc.addCliente(c)
      elif x == 2:
        x = int(input("Digite: \n1 se quiser buscar pelo nome\n2 se quiser buscar pelo cpf\n3 se quiser voltar\n"))
        while x != 1 and x != 2 and x != 3:
          print("Digite um valor válido\n")
          x = int(input("Digite: \n1 se quiser buscar pelo nome\n2 se quiser buscar pelo cpf\n3 se quiser voltar\n"))

        if x == 1:
          nome = input("Digite o nome do cliente: ")
          c = vc.buscaClienteNome(nome)
          return c
        elif x == 2:
          cpf = input("Digite o cpf do cliente: ")
          c = vc.buscaClienteCpf(cpf)
          retunr c
          
      x = int(input("Digite: \n0 para sair\n1 para cadastrar do cliente\n2 para buscar o cliente\n3 para voltar\n"))
      Persistencia(vc, 0, 0).escreveCliente()#sempre que eu finalizar eu o metodo eu faço a escrita? Ou isso será opcional?
