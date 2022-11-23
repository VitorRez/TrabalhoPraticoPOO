from entidade import Entidade

class Cliente(Entidade):
  def __init__(self, nome, telefone, endereco, cpf):
    super().__init__(cpf)
    self.nome = nome
    self.telefone = telefone
    self.endereco = endereco

  def retorna_nome(self):
    return self.nome

  def retorna_tel(self):
    return self.telefone

  def retorna_end(self):
    return self.endereco
  
  def retorna_cpf(self):
    return self.cpf

  def identificacao(self):
    print("Nome: ",self.nome, "Telefone: ", self.telefone, "Endereço: ", self.endereco, "cpf: ", self.id)
