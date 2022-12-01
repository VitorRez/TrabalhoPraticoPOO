from menuCliente import MenuCliente
from menuProduto import MenuProduto
from menuFornecedor import menuFornecedor
from menuVenda import menuVenda
from vetorCliente import VetorCliente
from vetorProduto import VetorProduto
from vetorFornecedor import vetorFornecedor
from vetorVenda import vetorVenda
from persistencia_cliente import persistencia_cliente
from persistencia_produto import persistencia_produto
from persistencia_fornecedores import persistencia_fornecedor
from persistencia_venda import persistencia_venda

class menu:
    def showmenu():
        comando = 5
        vc = VetorCliente()
        vp = VetorProduto()
        vf = vetorFornecedor()
        ve = vetorVenda()
        pc = persistencia_cliente(vc)
        pc.insercao(vc)
        pp = persistencia_produto(vp)
        pp.insercao(vp)
        pf = persistencia_fornecedor(vf)
        pf.insercao(vf)
        pe = persistencia_venda(ve)
        pe.insercao(ve)
        comando == 6
        print("---------------------------")
        print("         MR TOMATO         ")
        print("        horti-fruti        ")
        print("---------------------------")
        while comando != 0:
            #try: 
            print("---------------------------")
            print("      MENU PRINCIPAL       ")
            print("---------------------------")
            comando = int(input("Digite: \n0 Para sair\n1 Para gerenciar produtos\n2 Para gerenciar clientes\n3 Para gerenciar fornecedores\n4 Para realizar uma venda \n"))
            if comando == 1:
                print("---------------------------")
                print("  GERENCIADOR DE PRODUTOS  ")
                print("---------------------------")
                MenuProduto.menuP(vp, vf)
                pp.alteracao()
                pf.alteracao()
            if comando == 2:
                print("---------------------------")
                print("  GERENCIADOR DE CLIENTES  ")
                print("---------------------------")
                MenuCliente.menuC(vc)
                pc.alteracao()
            if comando == 3:
                print("---------------------------")
                print("GERENCIADOR DE FORNECEDORES")
                print("---------------------------")
                menuFornecedor.menuF(vf)
                pf.alteracao()
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
                    cd = 0
                    for i in ve.vendas:
                        cd += 1
                    menuVenda.menuV(ve, c, vp, cd)
                    cd += 1
                ve.listaVendas()
                pp.alteracao()
                pe.alteracao()
            if comando > 4 or comando < 0:
                print("Digite um comando válido!")
            #except:
                #print("Digite um comando válido!")

menu.showmenu()


