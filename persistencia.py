from entidade import Entidade
from cliente import Cliente
from vetorCliente import VetorCliente
from produto import Produto
from vetorProduto import VetorProduto

class Persistencia(Entidade):
  def __init__(self, vc, vp, vv):
    self.cliente = vc
    self.produto = vp
    self.venda = vv

  def escreveCliente(self):
    fileC = open("Cliente.txt", "w")#n esquecer de mudar para "a". Vale a pena mudar par "a"?
    
    for i in self.cliente.clientes:
      fileC.write(str(i.nome) + "\n")
      fileC.write(str(i.telefone) + "\n")
      fileC.write(str(i.endereco) + "\n")
      fileC.write(str(i.id) + "\n")
    
    fileC.close()
    #analisar o '\n' no arquivo

  def escreveProduto(self):
    fileP = open("Produto.txt", "a")

    for i in self.produto.Produtos:
      fileP.write(str(i.nome) + "\n")
      fileP.write(str(i.quantidade) + "\n")
      fileP.write(str(i.preco_unitario) + "\n")
      fileP.write(str(i.id) + "\n")
    
    fileP.close()

  def escreveVenda(self):
    fileV = open("Venda.txt", "a")
    
    for i in self.venda.carrinho:
      fileV.write(str(i.nome) + "\n")
      fileV.write(str(i.quantidade) + "\n")
      fileV.write(str(i.preco_unitario) + "\n")
      fileV.write(str(i.id) + "\n")
    
    fileV.close()

  def leCliente(self, vc):
    fileC = open("Cliente.txt", "r")
    lc = fileC.readlines()
    tam = 0
   
    while tam < len(lc)-1: #esse "-1" é para não considerar o "\n" q aparece no final
      c = Cliente(0, 0, 0, 0)

      c.nome = lc[tam]
      c.telefone = lc[tam+1]
      c.endereco = lc[tam+2]
      c.id = lc[tam+3]
      
      vc.addCliente(c)
      tam += 4
      del c

    fileC.close()

  def leProduto(self, vp):
    fileP = open("Produto.txt", "r")
    lp = fileP.readlines()
    tam = 0

    while tam < len(lp)-1:
      p = Produto(0, 0, 0, 0)

      p.nome = lp[tam]
      p.quantidade = lp[tam+1]
      p.preco_unitario = lp[tam+2]
      p.id = lp[tam+3]
      
      vp.addProduto(p)
      tam += 4
      del p

    fileP.close()

  def leVenda(self, vv):
    fileV = open("Venda.txt", "r")
    lv = fileV.readlines()
    tam = 0

    while tam < len(lv)-1:
      p = Produto(0, 0, 0, 0)

      p.nome = lv[tam]
      p.quantidade = lv[tam+1]
      p.preco_unitario = lv[tam+2]
      p.id = lv[tam+3]

      vv.carrinho.append(p)
      tam += 4
      del p

    fileV.close()

  def identificacao(self):
    print(self.nome, self.id, self.Quantidade, self.Total)
