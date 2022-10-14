from cliente import Cliente
from vetorProduto import VetorProduto, produto
from entidade import Entidade

class Venda(Entidade):
    #coloquei a inicialização da superclasse entidade
    #não chama o metodo vetorProduto, e sim um vetor produto
    def __init__ (self, vp):
        super().__init__('venda', 0) 
        self.estoque = vp
        self.carrinho = []

    #defini a identificação para a classe
    def identificacao(self):
        print(self.nome, self.carrinho)

    def menuVenda(self):
        comando = int(input("Sair: 0\nRemover Produto do carrinho: 1\nAdicionar produto no carrinho: 2\nAlterar quantidade de um produto: 3\nFinalizar compra: 4\nCancelar compra: 5"))
        while comando != 0:
            if comando == 1:
                metodo = int(input("Remover pelo codigo: 1\nRemover pelo nome: 2\n"))
                if metodo == 1:
                    codigo = int(input("Digite o código do produto: \n"))
                    prod = VetorProduto.buscarProdutoCodigo(codigo)
                    for p in self.carrinho:
                        if p.codigo == prod.codigo:
                            #remover p do carrinho
                            break
                        else:
                            print("Produto não está no carrinho")


                elif metodo == 2:
                    nome = int(input("Digite o nome do produto: \n"))
                    prod = VetorProduto.buscarProdutoNome(nome)
                    for p in self.carrinho:
                        if p.nome == prod.nome:
                            #remover p do carrinho
                            break
                        else:
                            print("Produto não está no carrinho")

                else:
                    print("Digite um valor válido")                
               

            elif comando == 2:
                metodo = int(input("Adicionar pelo codigo: 1\nAdicionar pelo nome: 2\n"))
                if metodo == 1:
                    codigo = int(input("Digite o código do produto: \n"))
                    prod = VetorProduto.buscarProdutoCodigo(codigo)
                    quantidade = int(input("Digite a quantidade do produto: \n"))
                    if quantidade > prod.quantidade:
                        print("Quantidade indisponível, tente novamente...")
                    else:
                        prod.quantidade = quantidade
                        self.carrinho.append(prod)
                
                    
                elif metodo == 2:
                    nome = input("Digite o nome do produto: \n")
                    prod = VetorProduto.buscarProdutoNome(nome)
                    quantidade = int(input("Digite a quantidade do produto: \n"))
                    if quantidade > prod.quantidade:
                        print("Quantidade indisponível, tente novamente...")
                    else:
                        prod.quantidade = quantidade
                        self.carrinho.append(prod)

                else:
                    print("Digite um valor válido")


            elif comando == 3:
                metodo = int(input("Remover pelo codigo: 1\nRemover pelo nome: 2\n"))
                if metodo == 1:
                    codigo = int(input("Digite o código do produto: \n"))
                    prod = VetorProduto.buscarProdutoNome(codigo)
                    for p in self.carrinho:
                        if p.codigo == prod.codigo:
                            pass
                            #remove p do carrinho
                    
                elif metodo == 2:
                    nome = int(input("Digite o nome do produto: \n"))
                    prod = VetorProduto.buscarProdutoNome(nome)
                    for p in self.carrinho:
                        if p.codigo == prod.codigo:
                            pass
                            #remove p do carrinho

                else:
                    print("Digite um valor válido")


            elif comando == 4:
                #percorrer o carrinho calculando o valor total e listando os produtos e suas quantidades
                valor_total = 0
                for p in self.carrinho:
                    valor_total = valor_total + p.quantidade * p.valor
                    print("Item: \n")
                    print("Quantidade: \n")    
                    print("Valor unitário: \n")
                    

            elif comando == 5:
                break
