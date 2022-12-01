from novapersistencia import persistencia
from Produto import produto
from vetorProduto import VetorProduto
from novaVenda import Venda
from Fornecedores import Fornecedor
from cliente import Cliente
from vetorVenda import vetorVenda
import csv

class persistencia_venda(persistencia):
    def __init__(self, ve):
        super().__init__(ve)

    def insercao(self, ve):

        with open("venda_1.csv", "r") as arquivo_csv1:
            leitor_csv = csv.DictReader(arquivo_csv1)
            for linha in leitor_csv:
                c = Cliente(linha['nome'], linha['telefone'], linha['endereco'], int(linha['cpf']))
                v = Venda(c, int(linha['codigo']))
                ve.addVenda(v)

        with open("venda_2.csv", "r") as arquivo_csv2:
            leitor_csv2 = csv.DictReader(arquivo_csv2)
            for i in ve.vendas:
                for linha in leitor_csv2:
                    if int(linha['carrinho']) == i.id:
                        f = Fornecedor(linha['fnome'], linha['fcnpj'], linha['ftelefone'], linha['fendereco'])
                        p = produto(linha['nome'], linha['codigo'], f, float(linha['precounitario']), int(linha['quantidade']))
                        i.carrinho.append(p)
        self.vetor = ve

    def alteracao(self):

        with open("venda_1.csv", "w") as arquivo_csv1:
            escreve_csv = csv.writer(arquivo_csv1)
            escreve_csv.writerow(['codigo','nome','telefone','endereco','cpf','carrinho'])
            contador = 0
            for i in self.vetor.vendas:
                escreve_csv.writerow([i.id, i.cliente.nome, i.cliente.telefone, i.cliente.endereco, i.cliente.id, contador])
                contador += 1

        with open("venda_2.csv", "w") as arquivo_csv2:
            escreve_csv2 = csv.writer(arquivo_csv2)
            escreve_csv2.writerow(['carrinho','nome','codigo','precounitario','quantidade','fnome','fcnpj','ftelefone','fendereco'])
            contador = 0
            for i in self.vetor.vendas:
                for j in i.carrinho:
                    #print(j.nome)
                    escreve_csv2.writerow([contador, j.nome, j.id, j.preco_unitario, j.quantidade, j.fornecedor.nome, j.fornecedor.id, j.fornecedor.telefone, j.fornecedor.endereco])
                contador += 1

    def exclusao(self):

        with open("venda_1.csv", "w") as arquivo_csv1:
            escreve_csv = csv.writer(arquivo_csv1)
            escreve_csv.writerow(['codigo','nome','telefone','endereco','cpf','carrinho'])

        with open("venda_2.csv", "w") as arquivo_csv2:
            escreve_csv = csv.writer(arquivo_csv2)
            escreve_csv.writerow(['carrinho','nome','codigo','precounitario','quantidade','f_nome','f_cnpj','f_telefone','f_endereco'])