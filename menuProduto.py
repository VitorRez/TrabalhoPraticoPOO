from Produto import produto
from vetorProduto import VetorProduto

class MenuProduto:
    def menuP(vp):
        x = int(input("Digite: \n0 Para sair \n1 Para cadastrar produto \n2 Busca produto \n3 Para listar produtos \n4 Remover produto \n5 Adicionar quantidade de um produto\n6 Retirar quantidade de um produto\n"))

        while x!=0 and x!=1 and x!=2 and x!=3 and x!=4 and x!=5 and x!=6:
            print("Digite um valor válido\n")
            x = int(input("Digite: \n0 Para sair \n1 Para cadastrar produto \n2 Busca produto \n3 Para listar produtos \n4 Remover produto \n5 Adicionar quantidade de um produto\n6 Retirar quantidade de um produto\n"))

        while x==1 or x==2 or x==3 or x==4 or x==5 or x==6:
            if x==0:
                break

            #Funcao de cadstrar produto
            elif x==1:
                nome = input("Digite o nome do produto: ")
                nome = nome.title()
                codigo = int(input("Digite o código do produto: "))
                precounitario = float(input("Digite o preço unitário do produto: "))
                quantidade = int(input("Digite a quantidade do produto: "))
                p = produto(nome, codigo, precounitario, quantidade)
                i = 0
                for x in vp.Produtos:
                    if x.nome == nome or x.id == codigo:
                        i = int(input("Produto ja cadastrado, deseja adicionar a quantidade inserida?\n1 Sim\n2 Não \n"))
                        if i == 1:
                            x.quantidade = x.quantidade + quantidade
                            break
                        if i == 2:
                            print("Estoque não será alterado para não comprometer o estoque atual")
                            break
                if i == 0:
                    vp.addProduto(p)

            #Funcao de buscar produto
            elif x==2:
                x = int(input("\nSe você quiser buscar: \nPor nome digite 1 \nPor código digite 2\n"))
                while x!=1 and x!=2:
                    print("Digite um valor válido\n")
                    x = int(input("\nSe você quiser buscar: \nPor nome digite 1 \nPor código digite 2\n"))
                if x==1:
                    nome = input("Digite o nome do produto: ")
                    nome = nome.title()
                    vp.buscarProdutoNome(nome)
                elif x==2:
                    codigo = int(input("Digite o código do produto: "))
                    vp.buscarProdutoCodigo(codigo)

            #função de listar produto, talvez seja desnecessario
            elif x==3:
                vp.listaProdutos()
                    
            #Funcao de excluir produto
            elif x==4:
                codigo = int(input("Digite o código do produto: "))
                vp.removerProdutoCodigo(codigo)

            elif x==5:
                x = int(input("Se você quiser Adicionar o produto:\nPor nome digite 1 \nPor código digite 2\n"))
                if x == 1:
                    nome = input("Digite o nome do produto: ")
                    nome = nome.title()
                    Qtd = int(input("Digite a quantidade do produto: "))
                    vp.adicionarProdutoNome(nome, Qtd)
                elif x == 2:
                    codigo = int(input("Digite o codigo do produto: "))
                    Qtd = int(input("Digite a quantidade do produto: "))
                    vp.adicionarProdutoCodigo(codigo, Qtd)

            elif x==6:    
                codigo = int(input("Digite o codigo do produto: "))
                Qtd = int(input("Digite a quantidade do produto: "))
                vp.venderProdutoCodigo(codigo, Qtd)
                

            x = int(input("Digite: \n0 Para sair \n1 Para cadastrar produto \n2 Busca produto \n3 Para listar produtos \n4 Remover produto\n5 Adicionar quantidade de um produto\n6 Retirar quantidade de um produto\n")) 