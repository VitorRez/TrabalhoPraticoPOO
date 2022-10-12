from menuCliente import MenuCliente
from menuProduto import MenuProduto
from vetorCliente import VetorCliente
from vetorProduto import VetorProduto

class menu:

    def showmenu():
        comando = 5
        vc = VetorCliente()
        vp = VetorProduto()
        while comando != 0:
            comando = int(input("Digite: \n0 para sair\n1 para gerenciar produtos\n2 para gerenciar clientes\n3 para realizar uma venda "))
            if comando == 1:
                MenuProduto.menuP(vp)
            if comando == 2:
                MenuCliente.menuC(vc)
            if comando == 3:
                #funções relacionadas as vendas
                print("fodeu")
            if comando > 3 or comando < 0:
                print("Digite um comando válido")
        
menu.showmenu()

