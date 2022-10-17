from persistência import persistencia
from vetorProduto import *
from cliente import *
from Produto import *
from vetorCliente import *
from entidade import *
from persistencia import *

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
        pe = Persistencia(0, vp, ve, 0)
        pe.leVenda(ve)
        comando = int(input("Sair: 0\nRemover Produto do carrinho: 1\nAdicionar produto no carrinho: 2\nAlterar quantidade de um produto: 3\nFinalizar compra: 4\nCancelar compra: 5\n"))
        if comando < 0 or comando > 5:
            comando = menuVenda.verifica_validade(comando, 0, 5)

        while comando != 0:
            if comando == 1:
                metodo = int(input("Remover pelo codigo: 1\nRemover pelo nome: 2\nVoltar: 3\n"))
                metodo = menuVenda.verifica_validade(metodo, 1, 3)
                
                
                if metodo == 1:
                    codigo = int(input("Digite o código do produto: \n"))
                    
                    for p in ve.carrinho: 
                        if p.id == codigo:
                            print(p.nome, " foi removido com sucesso\n")
                            ve.carrinho.remove(p)
                            #incrementar novamente a quantidade no estoque
                            vp.adicionarProdutoNome(p.nome, p.quantidade)
                            break

                elif metodo == 2:
                    nome = input("Digite o nome do produto: \n")
                    for p in ve.carrinho:
                        if p.nome == nome:
                            print(p.nome, " foi removido com sucesso\n")
                            ve.carrinho.remove(p)
                            #incrementar novamente a quantidade no estoque
                            vp.adicionarProdutoNome(p.nome, p.quantidade)
                            break
                            
                elif metodo == 3:
                    comando = 6
                    metodo = 6
                    continue

                pe.escreveProduto()
                pe.escreveVenda()

            elif comando == 2:
                metodo = int(input("Adicionar pelo codigo: 1\nAdicionar pelo nome: 2\nVoltar: 3\n"))
                metodo = menuVenda.verifica_validade(metodo, 1, 3)

                if metodo == 1:
                    codigo = int(input("Digite o código do produto: \n"))
                    Produto = vp.buscarProdutoCodigo(codigo)
                    x=0
                    while x == 0:
                        print(Produto.nome, "\nQuantidade disponível: ",Produto.quantidade, "\nValor Unitario: ", Produto.preco_unitario)
                        quantidade = int(input("Digite a quantidade do produto: "))
                        if quantidade > Produto.quantidade:
                            print("Quantidade do produto indisponível!\n")
                            x = int(input("Deseja alterar quantidade? \nSim: 1\nNão: 2\n"))
                            x = menuVenda.verifica_validade(x, 1, 2)
                            if x == 1:
                                x = 0
                            else:
                                continue
                        elif quantidade <= 0:
                            x = 0
                            print("Por favor digite um valor válido.\n")
                        else:
                            produto2 = produto(Produto.nome, Produto.id, Produto.preco_unitario, quantidade)
                            ve.carrinho.append(produto2)
                            vp.venderProdutoCodigo(Produto.id,quantidade)
                            x=1
                    pe.escreveProduto()
                
                    
                elif metodo == 2:
                    nome = input("Digite o nome do produto: ")
                    Produto = vp.buscarProdutoNome(nome)
                    x=0
                    while x == 0:
                        print(Produto.nome, "\nQuantidade disponível: ",Produto.quantidade, "\nValor Unitario: ", Produto.preco_unitario)
                        quantidade = int(input("Digite a quantidade do produto: "))
                        if quantidade > Produto.quantidade:
                            print("Quantidade do produto indisponível!\n")
                            x=int(input("Deseja alterar quantidade? \nSim: 1\nNão: 2\n"))
                            if x == 1:
                                x = 0
                            else:
                                continue
                        elif quantidade <= 0:
                            x = 0
                            print("Por favor digite um valor válido.\n")
                        else:
                            produto2 = produto(Produto.nome, Produto.id, Produto.preco_unitario, quantidade)
                            ve.carrinho.append(produto2)
                            vp.venderProdutoCodigo(Produto.id, quantidade)
                            x=1
                    pe.escreveProduto()
                
                elif metodo == 3:
                    comando = 6
                    metodo = 6
                    continue

                pe.escreveVenda()
            
            elif comando == 3:
                metodo = int(input("Alterar pelo código: 1\nAlterar pelo nome: 2\nVoltar: 3\n"))
                metodo = menuVenda.verifica_validade(metodo, 1, 3)


                if metodo == 1:
                    codigo = int(input("Digite o código do produto: \n"))
                    prod = vp.buscarProdutoCodigo(codigo)
                    new_qtd = int(input("Qual a nova quantidade? \n"))
                    for p in ve.carrinho:
                         
                        if p.id == prod.id:
                            if p.quantidade > new_qtd:
                                #incrementar quantidade do estoque
                                VetorProduto.adicionarProdutoNome(p.nome, new_qtd)
 
                            else:
                                #decrementar quantidade no estoque
                                VetorProduto.venderProdutoCodigo(p.id, new_qtd-p.quantidade)
                                
                            p.quantidade = new_qtd
                            print("Alterado com sucesso\n")
                    
                elif metodo == 2:
                    nome = input("Digite o nome do produto: ")
                    prod = vp.buscarProdutoNome(nome)
                    for p in ve.carrinho:
                        
                        if p.id == prod.id:
                            if p.quantidade > new_qtd:
                                #incrementar quantidade do estoque
                                VetorProduto.adicionarProdutoNome(p.nome, new_qtd)
 
                            else:
                                #decrementar quantidade no estoque
                                VetorProduto.venderProdutoCodigo(p.id, new_qtd-p.quantidade)
                                
                            p.quantidade = new_qtd
                            print("Alterado com sucesso\n")

                elif metodo == 3:
                    comando = 6
                    metodo = 6
                    continue
                pe.escreveVenda()
                pe.escreveProduto()

            elif comando == 4:
                #percorre o carrinho calculando o valor total e listando os produtos e suas quantidades
                x=int(input("Continuar: 1\nVoltar: 2\n"))
                x = menuVenda.verifica_validade(x, 1, 2)

                if x==1:
                    valor_total = 0
                    print("Cliente: ", ve.comprador.nome)
                    for p in ve.carrinho:
                        valor_total = valor_total + p.quantidade * p.preco_unitario
                        print("Item: ", p.nome)
                        print(", Quantidade: ", p.quantidade)    
                        print(", Valor unitário: \n", p.preco_unitario)

                    print("\nTotal da compra: ", valor_total)
                    print("\n")
                    ve.carrinho.clear()   
                else:
                    for p in ve.carrinho:
                        p1 = vp.buscarProdutoCodigo(p.id)
                        p1.quantidade += p.quantidade
                    ve.carrinho.clear()
                    pe.escreveVenda()
                    break
                pe.escreveVenda()
                pe.escreveProduto()

            elif comando == 5:
                x = int(input("Confirmar: 1\nVoltar: 2\n"))
                if x == 1:
                    for p in ve.carrinho:
                        p1 = vp.buscarProdutoCodigo(p.id)
                        p1.quantidade += p.quantidade
                    ve.carrinho.clear()
                    pe.escreveVenda()
                    break
                else:
                    break

            comando = int(input("Sair: 0\nRemover Produto do carrinho: 1\nAdicionar produto no carrinho: 2\nAlterar quantidade de um produto: 3\nFinalizar compra: 4\nCancelar compra: 5\n"))
            if comando < 0 or comando > 5:
                comando = menuVenda.verifica_validade(comando, 0, 5)
            
            
    def verifica_validade(var, inf, sup):
        while(var < inf or var > sup):
            var = int(input("Digite um valor válido!\n"))
        return var
