from vetorProduto import *
from cliente import *
from vetorCliente import *
from entidade import *

class Venda(Entidade):
    def __init__ (self, nome):
        super().__init__('venda', 0)
        self.comprador = nome
        self.carrinho = []

    def identificacao(self):
        for p in self.carrinho:
            print(p.nome, p.quantidade)



class menuVenda(Venda):

    def showMenu(vp, c):
        c.identificacao()
        ve = Venda(c)
        comando = int(input("Sair: 0\nRemover Produto do carrinho: 1\nAdicionar produto no carrinho: 2\nAlterar quantidade de um produto: 3\nFinalizar compra: 4\nCancelar compra: 5\n"))
        while comando != 0:
            if comando == 1:
                metodo = int(input("Remover pelo codigo: 1\nRemover pelo nome: 2\n"))
                if metodo == 1:
                    codigo = int(input("Digite o código do produto: "))
                    pos = 0 #posicao da lista que esta sendo feito a busca
                    for p in ve.carrinho: 
                        if p.id == codigo:
                            print(p.nome, " foi removido com sucesso")
                            ve.carrinho.remove(p)
                            #incrementar novamente a quantidade no estoque
                            break
                    
                

                elif metodo == 2:
                    nome = input("Digite o nome do produto: ")
                    
                    pos = 0 #posicao da lista que esta sendo feito a busca
                    for p in ve.carrinho:
                        if p.nome == nome:
                            print(p.nome, " foi removido com sucesso")
                            ve.carrinho.remove(p)
                            #incrementar novamente a quantidade no estoque
                            break
    
            elif comando == 2:
                metodo = int(input("Adicionar pelo codigo: 1\nAdicionar pelo nome: 2\n"))
                if metodo == 1:
                    codigo = int(input("Digite o código do produto: "))
                    Produto = vp.buscarProdutoCodigo(codigo)
                    print(Produto)
                    quantidade = int(input("Digite a quantidade do produto: "))
                    if quantidade > Produto.quantidade:
                        print("Quantidade do produto indisponível!\n")
                    else:
                        produto2 = produto(Produto.nome, Produto.id, Produto.preco_unitario, quantidade)
                        ve.carrinho.append(produto2)
                        vp.venderProdutoCodigo(Produto,quantidade)

                        
                
                    
                elif metodo == 2:
                    nome = input("Digite o nome do produto: ")
                    Produto = vp.buscarProdutoNome(nome)
                    print(Produto)
                    quantidade = int(input("Digite a quantidade do produto: "))
                    if quantidade > Produto.quantidade:
                        print("Quantidade do produto indisponível!")
                    else:
                        produto2 = produto(Produto.nome, Produto.id, Produto.preco_unitario, quantidade)
                        ve.carrinho.append(produto2)
                        vp.venderProdutoCodigo(Produto,quantidade)
                
            elif comando == 3:
                metodo = int(input("Alterar pelo código: 1\nAlterar pelo nome: 2\n"))
                if metodo == 1:
                    codigo = int(input("Digite o código do produto: "))
                    prod = vp.buscarProdutoCodigo(codigo)
                    print(prod)
                    new_qtd = int(input("Qual a nova quantidade? "))
                    for p in ve.carrinho:
                         
                        if p.codigo == prod.codigo:
                            if p.quantidade > new_qtd:
                                #decrementar quantidade do estoque
                                pass 
                            else:
                                #incrementar quantidade no estoque

                                pass
                            p.quantidade = new_qtd
            
                            print("Alterado com sucesso")
                            break
                    
                elif metodo == 2:
                    nome = int(input("Digite o nome do produto: "))
                    prod = vp.buscarProdutoNome(nome)
                    for p in ve.carrinho:
                        if p.nome == prod.nome:
                            if p.quantidade > new_qtd:
                                #decrementar quantidade do estoque
                                pass 
                            else:
                                #incrementar quantidade no estoque

                                pass
                            p.quantidade = new_qtd
            
                            print("Alterado com sucesso")
                            break


            elif comando == 4:
                #percorre o carrinho calculando o valor total e listando os produtos e suas quantidades
                valor_total = 0
                print("Cliente: ", ve.comprador.nome)
                for p in ve.carrinho:
                    valor_total = valor_total + p.quantidade * p.preco_unitario
                    print("Item: ", p.nome)
                    print("Quantidade: ", p.quantidade)    
                    print("Valor unitário: ", p.preco_unitario)

                print("\nTotal da compra: ", valor_total)
                ve.carrinho.clear()   

            elif comando == 5:
                ve.carrinho.clear()
                break

            comando = int(input("Sair: 0\nRemover Produto do carrinho: 1\nAdicionar produto no carrinho: 2\nAlterar quantidade de um produto: 3\nFinalizar compra: 4\nCancelar compra: 5\n"))
