from novaVenda import *
from vetorCliente import *
from vetorProduto import *
from cliente import *
from Produto import *

class menuVenda:
    def menuV(vve, c, vp, cd):
        ve = Venda(c, cd)
        comando = int(input("Sair: 0\nRemover Produto do carrinho: 1\nAdicionar produto no carrinho: 2\nAlterar quantidade de um produto: 3\nFinalizar compra: 4\nCancelar compra: 5\n"))
        if comando == 6:
                vve.listaVendas()
        if comando < 0 or comando > 5:
            comando = verifica_validade(comando, 0, 5)
            
        while comando != 0:
            if comando == 1:
                metodo = int(input("Remover pelo codigo: 1\nRemover pelo nome: 2\nVoltar: 3\n"))
                metodo = verifica_validade(metodo, 1, 3)
                if metodo == 1:
                    codigo = int(input("Digite o código do produto: "))
                    p = vp.buscaProdutoCodigo(codigo)
                    if p == None:
                        break
                    print(p.nome, " foi removido com sucesso")
                    ve.removeCarrinho(p.codigo)
                if metodo == 2:
                    nome = input("Digite o nome do produto: ")
                    p = vp.buscaProdutoNome(nome)
                    if p == None:
                        break
                    print(p.nome, " foi removido com sucesso")
                    ve.removeCarrinho(p.codigo)
        
            if comando == 2:
                metodo = int(input("Adicionar produto pelo código: 1\nAdicionar produto pelo nome: 2\nVoltar: 3\n"))
                metodo = verifica_validade(metodo, 1, 3)
                control = 0
                if metodo == 1:
                    codigo = int(input("Digite o código do produto: "))
                    quantidade = int(input("Digite a quantidade do produto: "))
                    control = ve.addCarrinhoCodigo(quantidade, vp, codigo)
                if metodo == 2: 
                    nome = input("Digite o nome do produto: ")
                    quantidade = int(input("Digite a quantidade do produto: "))
                    control = ve.addCarrinhoNome(quantidade, vp, nome)
                while control != 0:
                    if control == 1:
                        x = int(input("Deseja adicionar outro produto?\nSim: 1\nNão: 2\n"))
                        x = verifica_validade(x, 1, 2)
                        if x == 1:
                            if metodo == 1:
                                codigo = int(input("Digite o código do produto: "))
                                quantidade = int(input("Digite a quantidade do produto: "))
                                control = ve.addCarrinhoCodigo(quantidade, vp, codigo)
                            if metodo == 2:
                                nome = input("Digite o nome do produto: ")
                                quantidade = int(input("Digite a quantidade do produto: "))
                                control = ve.addCarrinhoNome(quantidade, vp, nome)
                        if x == 2:
                            break
                    if control == 2:
                        x = int(input("Quantidade indisponível, deseja alterá-la?\nSim: 1\nNão: 2\n"))
                        x = verifica_validade(x, 1, 2)
                        if x == 1:
                            if metodo == 1:
                                quantidade = int(input("Digite a quantidade do produto: "))
                                control = ve.addCarrinhoCodigo(quantidade, vp, codigo)
                            if metodo == 2:
                                quantidade = int(input("Digite a quantidade do produto: "))
                                control = ve.addCarrinhoNome(quantidade, vp, nome)
                        if x == 2:
                            break
        
            if comando == 3:
                metodo = int(input("Alterar pelo código: 1\nAlterar pelo nome: 2\nVoltar: 3\n"))
                metodo = verifica_validade(metodo, 1, 3)
                control = 0
                if metodo == 1:
                    codigo = int(input("Digite o código do produto: "))
                    quantidade = int(input("Digite a nova quantidade: "))
                    control = ve.alteraQntdCodigo(codigo, vp, quantidade)
                if metodo == 2:
                    nome = input("Digite o nome do produto: ")
                    quantidade = int(input("Digite a nova quantidade: "))
                    control = ve.alteraQntdNome(nome, vp, quantidade)
        
            if comando == 4:
                x=int(input("Continuar: 1\nVoltar: 2\n"))
                x = verifica_validade(x, 1, 2)
                if x == 1:
                    ve.finalizarVenda()
                    vve.addVenda(ve)
                if x == 2:
                    ve.cancelarVenda(vp)
        
            if comando == 5:
                x=int(input("Continuar: 1\nVoltar: 2\n"))
                x = verifica_validade(x, 1, 2)
                if x == 1:
                    ve.cancelarVenda(vp)
                if x == 2:
                    break
            comando = int(input("Sair: 0\nRemover Produto do carrinho: 1\nAdicionar produto no carrinho: 2\nAlterar quantidade de um produto: 3\nFinalizar compra: 4\nCancelar compra: 5\n"))
            if comando == 6:
                vve.listaVendas()
            if comando < 0 or comando > 5:
                comando = verifica_validade(comando, 0, 5)
            

def verifica_validade(var, inf, sup):
        while(var < inf or var > sup):
            var = int(input("Digite um valor válido!\n"))
        return var