from Produto import Produto
from vetorProduto import vetorProduto

class MenuProduto:
    def menu(vp):
        x = int(input("Digite: \n0 para sair \n1 para cadastrar produto \n2 busca produto \n3 para listar produtos \n4 remover produto \n5 Adicionar quantidade de um produto"))

        while x!=0 and x!=1 and x!=2 and x!=3 and x!=4 and x!=5:
            print("Digite um valor válido\n")
            x = int(input("Digite: \n0 para sair \n1 para cadastrar produto \n2 busca produto \n3 para listar produtos \n4 remover produto \n5 Adicionar quantidade de um produto"))

            while x==1 or x==2 or x==3 or x==4 or x==5:
                if x==0:
                    break

                #Funcao de cadstrar produto
                elif x==1:
                    nome = input("Digite o nome do produto: ")
                    codigo = input("Digite o código do produto: ")
                    precounitario = double(input("Digite o preço unitário do produto: "))
                    quantidade = int(input("Digite a quantidade do produto: "))
                    p = Produto(nome, codigo, precounitario, quantidade)
                    vp.addProduto(p)

                #Funcao de buscar produto
                elif x==2:
                    x = int(input("\nSe você quiser buscar: \nPor nome digite 1 \nPor código digite 2"))
                    while x!=1 and x!=2:
                        print("Digite um valor válido\n")
                        x = int(input("\nSe você quiser buscar: \nPor nome digite 1 \nPor código digite 2"))
                    if x==1:
                        nome = input("Digite o nome do produto")
                        vp.buscarProdutoNome(nome)
                    elif x==2:
                        codigo = input("Digite o código do produto\n")
                        vp.buscarProdutoCodigo(codigo)

                #função de listar produto, talvez seja desnecessario
                elif x==3:
                    listaProdutos()
                    
                #Funcao de excluir produto
                elif x==4:
                    removerProdutoCodigo(nome)

                elif x==5:
                    x = int(input("\nSe você quiser Adicionar o produto: \nPor nome digite 1 \nPor código digite 2"))
                    Qtd = int(input("\nDigite a quantidade do produto"))
                    if x == 1:
                        adicionarProdutoNome(nome, Qtd)
                    elif x == 2:
                        adicionarProdutoCodigo(nome, Qtd)

        x = int(input("Digite: \n0 para sair \n1 para cadastrar produto \n2 busca produto \n3 para listar produtos \n4 remover produto")) 