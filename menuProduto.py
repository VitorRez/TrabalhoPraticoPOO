from Produto import Produto
from vetorProduto import vetorProduto

class MenuProduto:
    def menu(vp):
        x = int(input("Digite: \n0 para sair \n1 para cadastrar produto \n2 busca produto \n3 para listar produtos \n4 remover produto"))

        while x!=0 and x!=1 and x!=2 and x!=3 and x!=4:
            print("Digite um valor válido\n")
            x = int(input("Digite: \n0 para sair \n1 para cadastrar produto \n2 busca produto \n3 para listar produtos \n4 remover produto"))

            while x==1 or x==2 or x==3 or x==4:
                if x==0:
                    break
                elif x==1:
                    nome = input("Digite o nome do produto: ")
                    codigo = input("Digite o código do produto: ")
                    precounitario = double(input("Digite o preço unitário do produto: "))
                    quantidade = int(input("Digite a quantidade do produto: "))
                    p = Produto(nome, codigo, precounitario, quantidade)
                    vp.addProduto(p)
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
                #elif x==3:
                    #função de listar produto

                #elif x==4:
                    #função de remover produto

        x = int(input("Digite: \n0 para sair \n1 para cadastrar produto \n2 busca produto \n3 para listar produtos \n4 remover produto")) 