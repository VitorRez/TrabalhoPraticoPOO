from menuCliente import MenuCliente
from vetorCliente import VetorCliente

class menu:

    def showmenu():
        comando = 5
        vc = VetorCliente()
        while comando != 0:
            comando = int(input("Encerrar: 0\nGerenciamento de produtos: 1\nGerenciamento de clientes: 2\nRealizar venda: 3\n"))
            if comando == 1:
                #funções relacionadas aos produtos
                print("tamo falido")
            if comando == 2:
                MenuCliente.menuC(vc)
            if comando == 3:
                #funções relacionadas as vendas
                print("fodeu")
            if comando > 3 or comando < 0:
                print("Digite um comando válido")
        
menu.showmenu()