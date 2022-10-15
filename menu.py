from menuCliente import MenuCliente
from menuProduto import MenuProduto
from menuFornecedor import menuFornecedor
from vetorCliente import VetorCliente
from vetorProduto import VetorProduto
from vetorFornecedor import vetorFornecedor
from Venda import Venda, menuVenda
from cliente import Cliente

class menu:
    def showmenu():
        comando = 5
        vc = VetorCliente()
        vp = VetorProduto()
        vf = vetorFornecedor()
        while comando != 0:
            print("---------------------------")
            print("      MENU PRINCIPAL       ")
            print("---------------------------")
            comando = int(input("Digite: \n0 para sair\n1 para gerenciar produtos\n2 para gerenciar clientes\n3 para gerenciar fornecedores\n4 para realizar uma venda \n"))
            if comando == 1:
                print("---------------------------")
                print("  GERENCIADOR DE PRODUTOS  ")
                print("---------------------------")
                MenuProduto.menuP(vp)
            if comando == 2:
                print("---------------------------")
                print("  GERENCIADOR DE CLIENTES  ")
                print("---------------------------")
                MenuCliente.menuC(vc)
            if comando == 3:
                print("---------------------------")
                print("GERENCIADOR DE FORNECEDORES")
                print("---------------------------")
                menuFornecedor.menuF(vf)
            if comando == 4:
                print("---------------------------")
                print("       REALIZAR VENDA      ")
                print("---------------------------")
                x = int(input("Deseja buscar o cliente por nome ou por cpf?\n1 nome\n2 codigo\n"))
                if x == 1:
                    nome = input("Digite o nome do cliente: ")
                    c = vc.buscaClienteNome(nome)
                if x == 2:
                    cpf = int(input("Digite o cpf do cliente: "))
                    c = vc.buscaClienteCpf(cpf)
                menuVenda.showMenu(vp, c)
            if comando > 4 or comando < 0:
                print("Digite um comando válido")
        
menu.showmenu()

