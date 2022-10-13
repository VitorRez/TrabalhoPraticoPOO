from cliente import cliente
from vetorProduto import VetorProduto
from Produto import produto
from entidade import Entidade

class Venda(Entidade):
    def __init__ (self):
        self.carrinho = []

    def Qtd_Prod(self, Quantidade):
        self.Quantidade = Quantidade

    def Total_Valor(self, Total):
        self.Total = Total
            
    def Codigo(self, IdProduto):
        self.IdProduto = IdProduto

    def retorna_Codigo(self):
        return self.IdProduto

    def retorna_Quantidade(self):
        return self.Quantidade

    def retorna_Total(self):
        return self.Total


class menuVenda(Venda):
    def __init__(self):
        menuVenda.showMenu()


    def showMenu(self, vetorProduto):
        self.produtos = []
        self.produtos = vetorProduto
        comando = int(input("Sair: 0\nRemover Produto do carrinho: 1\nAdicionar produto no carrinho: 2\nAlterar quantidade de um produto: 3\nFinalizar compra: 4\nCancelar compra: 5"))
        while comando != 0:
            if comando == 1:
                metodo = int(input("Remover pelo codigo: 1\nRemover pelo nome: 2\n"))
                if metodo == 1:
                    codigo = int(input("Digite o código do produto: \n"))
                    prod = VetorProduto.buscarProdutoCodigo(codigo)
                    pos = 0 #posicao da lista que esta sendo feito a busca
                    for p in self.carrinho:
                         
                        if p.codigo == prod.codigo:
                            print(self.carrinho.pop(pos), " foi removido com sucesso")
                            break
                        pos = pos + 1
                

                elif metodo == 2:
                    nome = int(input("Digite o nome do produto: \n"))
                    prod = VetorProduto.buscarProdutoNome(nome)
                    pos = 0 #posicao da lista que esta sendo feito a busca
                    for p in self.carrinho:
                        if p.nome == prod.nome:
                            print(self.carrinho.pop(pos), " foi removido com sucesso")
                            break
                        pos = pos + 1

                else:
                    print("Digite um valor válido")                
               
            elif comando == 2:
                metodo = int(input("Adicionar pelo codigo: 1\nAdicionar pelo nome: 2\n"))
                if metodo == 1:
                    codigo = int(input("Digite o código do produto: \n"))
                    #prod = VetorProduto.buscarProdutoCodigo(codigo)
                    quantidade = int(input("Digite a quantidade do produto: \n"))
                    if quantidade > prod.quantidade:
                        print("Quantidade do produto indisponível!\n")
                    else:
                        vetorProduto.venderProdutoCodigo(prod,quantidade)
                        prod.quantidade = quantidade
                        self.carrinho.append(prod)
                
                    
                elif metodo == 2:
                    nome = int(input("Digite o nome do produto: \n"))
                    #prod = VetorProduto.buscarProdutoNome(nome)
                    quantidade = int(input("Digite a quantidade do produto: \n"))
                    if quantidade > prod.quantidade:
                        print("Quantidade do produto indisponível!")
                    else:
                        vetorProduto.venderProdutoCodigo(prod,quantidade)
                        prod.quantidade = quantidade
                        self.carrinho.append(prod)

                else:
                    print("Digite um valor válido")

            elif comando == 3:
                metodo = int(input("Alterar pelo código: 1\nAlterar pelo nome: 2\n"))
                if metodo == 1:
                    codigo = int(input("Digite o código do produto: \n"))
                    prod = VetorProduto.buscarProdutoNome(codigo)
                    pos = 0 #posicao da lista que esta sendo feito a busca
                    for p in self.carrinho:
                         
                        if p.codigo == prod.codigo:
                            prod.quantidade = quantidade
                            self.carrinho[pos] = prod
                            print("Alterado com sucesso")
                            break
                        pos = pos + 1
                    
                elif metodo == 2:
                    nome = int(input("Digite o nome do produto: \n"))
                    prod = VetorProduto.buscarProdutoNome(nome)
                    pos = 0 #posicao da lista que esta sendo feito a busca
                    for p in self.carrinho:
                         
                        if p.nome == prod.nome:
                            prod.quantidade = quantidade
                            self.carrinho[pos] = prod
                            print("Alterado com sucesso")
                            break
                        pos = pos + 1


            elif comando == 4:
                #percorre o carrinho calculando o valor total e listando os produtos e suas quantidades
                valor_total = 0
                for p in self.carrinho:
                    valor_total = valor_total + p.quantidade * p.valor
                    print("Item: \n")
                    print("Quantidade: \n")    
                    print("Valor unitário: \n")      

                print("Total da compra: ", valor_total)   

            elif comando == 5:
                self.carrinho.clear()
                break
