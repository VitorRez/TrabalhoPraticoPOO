from Produto import produto
from vetorProduto import VetorProduto

class MenuProduto:
    def menuP(vp):
        x = int(input("Digite: \n0 para sair \n1 para cadastrar produto \n2 busca produto \n3 para listar produtos \n4 remover produto \n"))

        while x!=0 and x!=1 and x!=2 and x!=3 and x!=4:
            print("Digite um valor válido\n")
            x = int(input("Digite: \n0 para sair \n1 para cadastrar produto \n2 busca produto \n3 para listar produtos \n4 remover produto \n"))

        while x==1 or x==2 or x==3 or x==4:
            if x==0:
                break

            #Funcao de cadstrar produto
            elif x==1:
                nome = input("Digite o nome do produto: ")
                codigo = int(input("Digite o código do produto: "))
                precounitario = float(input("Digite o preço unitário do produto: "))
                quantidade = int(input("Digite a quantidade do produto: "))
                p = produto(nome, codigo, precounitario, quantidade)
                vp.addProduto(p)

            #Funcao de buscar produto
            elif x==2:
                x = int(input("Se você quiser buscar: \nPor nome digite 1 \nPor código digite 2\n"))
                while x!=1 and x!=2:
                    print("Digite um valor válido\n                                                            ")
                    x = int(input("Se você quiser buscar: \nPor nome digite 1 \nPor código digite 2\n"))
                if x==1:
                    nome = input("Digite o nome do produto: ")
                    vp.buscarProdutoNome(nome)
                elif x==2:
                    codigo = int(input("Digite o código do produto: "))
                    vp.buscarProdutoCodigo(codigo)

            #função de listar produto, talvez seja desnecessario
            elif x==3:
                vp.listaProdutos()
                    
            #Funcao de excluir produto
            elif x==4:
                x = int(input("Se você quiser Excluir o produto: \nPor nome digite 1 \nPor código digite 2 \n"))
                if x == 1:
                    nome = input("Digite o nome do produto: ")
                    vp.removerProdutoNome(nome)
                elif x == 2:
                    codigo = int(input("Digite o código do produto: "))
                    vp.removerProdutoCodigo(codigo)

            x = int(input("Digite: \n0 para sair \n1 para cadastrar produto \n2 busca produto \n3 para listar produtos \n4 remover produto \n")) 

