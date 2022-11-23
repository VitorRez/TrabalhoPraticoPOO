from novapersistencia import persistencia
from Produto import produto
from Fornecedores import Fornecedor
from vetorProduto import VetorProduto
import csv

class persistencia_produto(persistencia):
    def __init__(self, vp):
        super().__init__(vp)

    def insercao(self, vp):

        with open("Produtos.csv", "r") as arquivo_csv:
            leitor_csv = csv.DictReader(arquivo_csv)

            for linha in leitor_csv:
                f = Fornecedor(linha['f_nome'], linha['f_cnpj'], linha['f_telefone'], linha['f_endereco'])
                p = produto(linha['nome'], linha['codigo'], f, linha['precounitario'], linha['quantidade'])
                vp.addProduto(p)

    def alteracao(self):

        with open("Produtos.csv", "w") as arquivo_csv:
            escreve_csv = csv.writer(arquivo_csv)
            escreve_csv.writerow(['nome'],['codigo'],['precounitario'],['quantidade'],['f_nome'],['f_cnpj'],['f_telefone'],['f_endereco'])


            for i in self.v:
                escreve_csv.writerow([i.nome],[i.id],[i.precounitario],[i.quantidade],[i.fornecedor.nome],[i.fornecedor.id],[i.fornecedor.telefone],[i.fornecedor.endereco])

    def exclusao(self):

        with open("Produtos.csv", "w") as arquivo_csv:
            escreve_csv = csv.writer(arquivo_csv)
            escreve_csv.writerow(['nome'],['codigo'],['precounitario'],['quantidade'],['f_nome'],['f_cnpj'],['f_telefone'],['f_endereco'])

            self.v.clear()
            