from entidade import Entidade
from cliente import Cliente
from vetorCliente import VetorCliente

class Persistencia(Entidade):
  def __init__(self, vc, produto, venda):
    self.cliente = vc
    self.produto = produto
    self.venda = venda

  def escreveCliente(self, vc):
    fileC = open("Cliente.txt", "w")#n esquecer de mudar para "a". Vale a pena mudar par "a"?
    
    for i in vc.clientes:
      fileC.write(i.nome + "\n")
      fileC.write(i.telefone + "\n")
      fileC.write(i.endereco + "\n")
      fileC.write(i.id + "\n")
    
    fileC.close()
    #analisar o '\n' no arquivo

  def escreveProduto(self, produto):
    fileP = open("Produto.txt", "a")
    #olhar depois os atributos de produto
    fileP.close()

  def escreveVenda(self, venda):
    fileV = open("Venda.txt", "a")
    #olhar depois os atributos de venda
    fileV.close()

  def leCliente(self, vc):
    fileC = open("Cliente.txt", "r")
    lc = fileC.readlines()
    #print(lc)
    tam = 0
   
    while tam < len(lc)-1: #esse "-1" é para não considerar o "\n" q aparece no final
      c = Cliente(0, 0, 0, 0)

      c.nome = lc[tam]
      c.telefone = lc[tam+1]
      c.endereco = lc[tam+2]
      c.id = lc[tam+3]

      #print(c.nome, c.telefone, c.endereco, c.id)
      
      vc.addCliente(c)
      tam += 4
      del c #acredito q n esteja dando problema de memoria

    fileC.close()

  def leProduto(self, vp):
    print()

  def leVenda(self, vv):
    print()

  def identificacao(self):
    print(self.nome, self.id, self.Quantidade, self.Total)