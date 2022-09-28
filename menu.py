class menu:

    def showmenu():
        comando = 5
        while comando != 0:
            comando = int(input("Encerrar: 0\nGerenciamento de produtos: 1\nGerenciamento de clientes: 2\nRealizar venda: 3\n"))
            if comando == 1:
                #funções relacionadas aos produtos
                print("tamo falido")
            if comando == 2:
                #funções relacionadas aos clientes
                print("tamo sem cliente")
            if comando == 3:
                #funções relacionadas as vendas
                print("fodeu")
            if comando > 3 or comando < 0:
                print("Digite um comando válido")
        
menu.showmenu()