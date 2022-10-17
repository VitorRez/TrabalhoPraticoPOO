from menuCliente import MenuCliente
from menuProduto import MenuProduto
from menuFornecedor import menuFornecedor
from vetorCliente import VetorCliente
from vetorProduto import VetorProduto
from vetorFornecedor import vetorFornecedor
from Venda import Venda, menuVenda
from cliente import Cliente
from persistencia import *

class menu:
    def showmenu():
        comando = 5
        vc = VetorCliente()
        vp = VetorProduto()
        vf = vetorFornecedor()
        ve = []
        p = Persistencia(vc, vp, ve, vf)
        p.leCliente(vc)
        p.leProduto(vp)
        p.leFornecedores(vf)
        comando == 6
        print("---------------------------")
        print("         MR TOMATO         ")
        print("        horti-fruti        ")
        print("---------------------------")
        while comando != 0:
            try: 
                print("---------------------------")
                print("      MENU PRINCIPAL       ")
                print("---------------------------")
                comando = int(input("Digite: \n0 Para sair\n1 Para gerenciar produtos\n2 Para gerenciar clientes\n3 Para gerenciar fornecedores\n4 Para realizar uma venda \n"))
                if comando == 1:
                    print("---------------------------")
                    print("  GERENCIADOR DE PRODUTOS  ")
                    print("---------------------------")
                    MenuProduto.menuP(vp)
                    p.escreveProduto()
                if comando == 2:
                    print("---------------------------")
                    print("  GERENCIADOR DE CLIENTES  ")
                    print("---------------------------")
                    MenuCliente.menuC(vc)
                    p.escreveCliente()
                if comando == 3:
                    print("---------------------------")
                    print("GERENCIADOR DE FORNECEDORES")
                    print("---------------------------")
                    menuFornecedor.menuF(vf)
                    p.escreveFornecedores()
                if comando == 4:
                    print("---------------------------")
                    print("       REALIZAR VENDA      ")
                    print("---------------------------")
                    x = int(input("Deseja buscar o cliente por nome ou por cpf?\n1 Nome\n2 cpf\n"))
                    if x == 1:
                        nome = input("Digite o nome do cliente: ")
                        c = vc.buscaClienteNome(nome)
                    if x == 2:
                        cpf = int(input("Digite o cpf do cliente: "))
                        c = vc.buscaClienteCpf(cpf)
                    if c != None:
                        menuVenda.showMenu(vp, c)
                    p.escreveProduto()
                if comando > 4 or comando < 0:
                    print("Digite um comando válido!")
            except:
                print("Digite um comando válido!")

menu.showmenu()


