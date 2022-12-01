from novapersistencia import persistencia
from cliente import Cliente
from vetorCliente import VetorCliente
import csv

class persistencia_cliente(persistencia):
    def __init__(self, vc):
        super().__init__(vc)

    def insercao(self, vc):
        
        with open("Cliente.csv", "r") as arquivo_csv:
            leitor_csv = csv.DictReader(arquivo_csv)

            for linha in leitor_csv:
                c = Cliente(linha['nome'],linha['telefone'],linha['endereco'],linha['cpf'])
                vc.addCliente(c)
            self.vetor = vc

    def alteracao(self):

        with open("Cliente.csv", "w") as arquivo_csv:
            escreve_csv = csv.writer(arquivo_csv)
            escreve_csv.writerow(['nome','telefone','endereco','cpf'])
            
            for i in self.vetor.clientes:
                escreve_csv.writerow([i.nome,i.telefone,i.endereco,i.id])

    def exclusao(self):
        
        with open("Cliente.csv", "w") as arquivo_csv:
            escreve_csv = csv.writer(arquivo_csv)
            escreve_csv.writerow(['nome','telefone','endereco','cpf'])

        self.vetor.clear()


