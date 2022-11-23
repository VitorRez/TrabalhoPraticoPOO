from entidade import Entidade
from cliente import Cliente
from vetorCliente import VetorCliente
from Produto import produto
from vetorProduto import VetorProduto
from Fornecedores import Fornecedor
from vetorFornecedor import vetorFornecedor

class Persistencia(Entidade):
  def __init__(self, vc, vp, vv, vf):
    self.cliente = vc
    self.produto = vp
    self.venda = vv
    self.fornecedores = vf

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
    fileP = open("Produto.txt", "w")

    for i in self.produto.Produtos:
      fileP.write(str(i.nome) + "\n")
      fileP.write(str(i.quantidade) + "\n")
      fileP.write(str(i.preco_unitario) + "\n")
      fileP.write(str(i.id) + "\n")
      fileP.write(str(i.fornecedor.nome) + "\n")
      fileP.write(str(i.fornecedor.cnpj) + "\n")
      fileP.write(str(i.fornecedor.telefone) + "\n")
      fileP.write(str(i.fornecedor.endereco) + "\n")
    
    fileP.close()
  
  def escreveFornecedores(self):
    fileC = open("Fornecedores.txt", "w")#n esquecer de mudar para "a". Vale a pena mudar par "a"?
    
    for i in self.fornecedores.Fornecedores:
      fileC.write(str(i.nome) + "\n")
      fileC.write(str(i.telefone) + "\n")
      fileC.write(str(i.endereco) + "\n")
      fileC.write(str(i.id) + "\n")
    
    fileC.close()

  def escreveVenda(self):
    fileV = open("Venda.txt", "w")
    
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

      c.nome = lc[tam].strip()
      c.telefone = lc[tam+1].strip()
      c.endereco = lc[tam+2].strip()
      c.id = int(lc[tam+3])
      
      vc.addCliente(c)
      tam += 4
      del c

    fileC.close()

  def leProduto(self, vp):
    fileP = open("Produto.txt", "r")
    lp = fileP.readlines()
    tam = 0

    while tam < len(lp)-1:
      p = produto(0, 0, 0, 0, 0)

      p.nome = lp[tam].strip()
      p.quantidade = int(lp[tam+1])
      p.preco_unitario = float(lp[tam+2])
      p.id = int(lp[tam+3])
      f = Fornecedor(lp[tam+4].strip(),int(lp[tam+5]),lp[tam+6].strip(),lp[tam+7].strip())
      p.fornecedor = f
      
      vp.addProduto(p)
      tam += 8
      del p
      del f

    fileP.close()

  def leFornecedores(self, vf):
    fileC = open("Fornecedores.txt", "r")
    lf = fileC.readlines()
    tam = 0
   
    while tam < len(lf)-1: #esse "-1" é para não considerar o "\n" q aparece no final
      f = Fornecedor(0, 0, 0, 0)

      f.nome = lf[tam].strip()
      f.telefone = lf[tam+1].strip()
      f.endereco = lf[tam+2].strip()
      f.id = int(lf[tam+3])
      
      vf.addFornecedor(f)
      tam += 4
      del f

    fileC.close()

  def leVenda(self, vv):
    fileV = open("Venda.txt", "r")
    lv = fileV.readlines()
    tam = 0

    while tam < len(lv)-1:
      p = produto(0, 0, 0, 0, 0)

      p.nome = lv[tam].strip()
      p.quantidade = int(lv[tam+1])
      p.preco_unitario = float(lv[tam+2])
      p.id = int(lv[tam+3])

      vv.carrinho.append(p)
      tam += 4
      del p

    fileV.close()

  def identificacao(self):
    print(self.nome, self.id, self.Quantidade, self.Total)
