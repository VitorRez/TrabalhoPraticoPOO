from menuCliente import MenuCliente
from menuProduto import MenuProduto
from vetorCliente import VetorCliente
from vetorProduto import VetorProduto
from Venda import Venda

class menu:
    def showmenu():
        comando = 5
        vc = VetorCliente()
        vp = VetorProduto()
        while comando != 0:
            print("--------------------------")
            print("      MENU PRINCIPAL      ")
            print("--------------------------")
            comando = int(input("Digite: \n0 para sair\n1 para gerenciar produtos\n2 para gerenciar clientes\n3 para realizar uma venda \n"))
            if comando == 1:
                print("--------------------------")
                print(" GERENCIADOR DE PRODUTOS  ")
                print("--------------------------")
                MenuProduto.menuP(vp)
            if comando == 2:
                print("--------------------------")
                print(" GERENCIADOR DE CLIENTES  ")
                print("--------------------------")
                MenuCliente.menuC(vc)
            if comando == 3:
                print("--------------------------")
                print("      REALIZAR VENDA      ")
                print("--------------------------")
                ve = Venda(vp)
                ve.menuVenda()
            if comando > 3 or comando < 0:
                print("Digite um comando válido")
        
menu.showmenu()

