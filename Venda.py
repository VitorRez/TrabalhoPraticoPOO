from cliente import cliente
from vetorProduto import VetorProduto, produto
from entidade import Entidade

class Venda(Entidade):
    def __init__ (self, vetorProduto):
        self.estoque = [] 
        self.estoque = vetorProduto
        self.carrinho = []
        menuVenda.showMenu()

    #defini a identificação para a classe
    def identificacao(self):
        print(self.nome, self.carrinho)


class menuVenda(Venda):
    def __init__(self, vetorProduto):
        self.produtos = []
        self.produtos = vetorProduto


    def showMenu(self):
        comando = int(input("Sair: 0\nRemover Produto do carrinho: 1\nAdicionar produto no carrinho: 2\nAlterar quantidade de um produto: 3\nFinalizar compra: 4\nCancelar compra: 5"))
        while comando != 0:
            if comando == 1:
                metodo = int(input("Remover pelo codigo: 1\nRemover pelo nome: 2\n"))
                if metodo == 1:
                    codigo = int(input("Digite o código do produto: \n"))
                    
                    pos = 0 #posicao da lista que esta sendo feito a busca
                    for p in Venda.carrinho:
                         
                        if p.codigo == codigo:
                            print(Venda.carrinho.pop(pos), " foi removido com sucesso")
                            #incrementar novamente a quantidade no estoque
                            break
                        pos = pos + 1
                

                elif metodo == 2:
                    nome = int(input("Digite o nome do produto: \n"))
                    
                    pos = 0 #posicao da lista que esta sendo feito a busca
                    for p in Venda.carrinho:
                        if p.nome == nome:
                            print(Venda.carrinho.pop(pos)," foi removido com sucesso")
                            #incrementar novamente a quantidade no estoque
                            break
                        pos = pos + 1
    
            elif comando == 2:
                metodo = int(input("Adicionar pelo codigo: 1\nAdicionar pelo nome: 2\n"))
                if metodo == 1:
                    codigo = int(input("Digite o código do produto: \n"))
                    produto = vetorProduto.buscarProdutoCodigo(codigo)
                    print(produto)
                    quantidade = int(input("Digite a quantidade do produto: \n"))

                    if quantidade > prod.quantidade:
                        print("Quantidade do produto indisponível!\n")
                    else:
                        vetorProduto.venderProdutoCodigo(prod,quantidade)
                        prod.quantidade = quantidade
                        Venda.carrinho.append(prod)

                        
                
                    
                elif metodo == 2:
                    nome = int(input("Digite o nome do produto: \n"))
                    prod = VetorProduto.buscarProdutoNome(nome)
                    quantidade = int(input("Digite a quantidade do produto: \n"))
                    if quantidade > prod.quantidade:
                        print("Quantidade do produto indisponível!")
                    else:
                        vetorProduto.venderProdutoNome(nome,quantidade)
                        prod.quantidade = quantidade
                        Venda.carrinho.append(prod)
                        #decrementar quantidade adicionada ao carrinho
                
            elif comando == 3:
                metodo = int(input("Alterar pelo código: 1\nAlterar pelo nome: 2\n"))
                if metodo == 1:
                    codigo = int(input("Digite o código do produto: \n"))
                    prod = vetorProduto.buscarProdutoNome(codigo)
                    print(prod)
                    new_qtd = int(input("Qual a nova quantidade?\n"))
                    pos = 0 #posicao da lista que esta sendo feito a busca
                    for p in Venda.carrinho:
                         
                        if p.codigo == prod.codigo:
                            if prod.quantidade > new_qtd:
                                #decrementar quantidade do estoque
                                pass 
                            else:
                                #incrementar quantidade no estoque
                                pass
                            prod.quantidade = new_qtd
                            Venda.carrinho[pos] = prod
                            print("Alterado com sucesso")
                            break
                        pos = pos + 1
                    
                elif metodo == 2:
                    nome = int(input("Digite o nome do produto: \n"))
                    prod = vetorProduto.buscarProdutoNome(nome)
                    pos = 0 #posicao da lista que esta sendo feito a busca
                    for p in Venda.carrinho:
                         
                        if p.nome == prod.nome:
                            if prod.quantidade > new_qtd:
                                #decrementar quantidade do estoque
                                pass 
                            else:
                                #incrementar quantidade no estoque
                                pass
                            prod.quantidade = quantidade
                            Venda.carrinho[pos] = prod
                            print("Alterado com sucesso")
                            break
                        pos = pos + 1


            elif comando == 4:
                #percorre o carrinho calculando o valor total e listando os produtos e suas quantidades
                valor_total = 0
                for p in Venda.carrinho:
                    valor_total = valor_total + p.quantidade * p.valor
                    print("Item: \n", p.nome)
                    print("Quantidade: \n". p.quantidade)    
                    print("Valor unitário: \n", p.valorunitario)

                print("\nTotal da compra: ", valor_total)   

            elif comando == 5:
                Venda.carrinho.clear()
                break

