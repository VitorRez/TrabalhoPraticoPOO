from entidade import Entidade

class Cliente(Entidade):
  def __init__(self, nome, telefone, endereco, cpf):
    super().__init__(cpf, nome)
    self.telefone = telefone
    self.endereco = endereco

  #"""def nome_clt(self, nome):
  #  self.nome = nome

  #def tel_clt(self, telefone):
  #  self.telefone = telefone

  #def end_clt(self, endereco):
  #  self.endereco = endereco

  #def cpf_clt(self, cpf):
  #  self.cpf = cpf"""

  def retorna_nome(self):
    return self.nome

  def retorna_tel(self):
    return self.telefone

  def retorna_end(self):
    return self.endereco
  
  def retorna_cpf(self):
    return self.cpf

  def identificacao(self):
    return self.Entidade.nome
