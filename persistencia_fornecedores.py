from novapersistencia import persistencia
from Fornecedores import Fornecedor
from vetorFornecedor import vetorFornecedor
import csv

class persistencia_fornecedor(persistencia):
    def __init__(self, vf):
        super().__init__(vf)

    def insercao(self, vf):

        with open("Fornecedores.csv", "r") as arquivo_csv:
            leitor_csv = csv.DictReader(arquivo_csv)

            for linha in leitor_csv:
                f = Fornecedor(linha['nome'], int(linha['cnpj']), linha['telefone'], linha['endereco'])
                vf.addFornecedor(f)
            self.vetor = vf

    def alteracao(self):

        with open("Fornecedores.csv", "w") as arquivo_csv:
            escreve_csv = csv.writer(arquivo_csv)
            escreve_csv.writerow(['nome','cnpj','telefone','endereco'])

            for i in self.vetor.Fornecedores:
                escreve_csv.writerow([i.nome, i.id, i.telefone, i.endereco])

    def exclusao(self):

        with open("Fornecedores.csv", "w") as arquivo_csv:
            escreve_csv = csv.writer(arquivo_csv)
            escreve_csv.writerow(['nome','cnpj','telefone','endereco'])

            self.vetor.clear()    