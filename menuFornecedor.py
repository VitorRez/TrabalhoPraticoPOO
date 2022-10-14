from Fornecedor import Fornecedor
from VetorFornecedor import VetorFornecedor

class menuFornecedor(vf):
    x = int(input("Digite: \n0 Para sair \n1 Para cadastrar Fornecedor \n2 Buscar Fornecedor \n3 Para listar Fornecedores \n4 Remover Fornecedores"))
    while x!=0 and x!=1 and x!=2 and x!=3 and x!=4:
        print("Digite um valor válido\n")
        x = int(input("Digite: \n0 Para sair \n1 Para cadastrar Fornecedor \n2 Buscar Fornecedor \n3 Para listar Fornecedores \n4 Remover Fornecedores"))
    
    while x==1 or x==2 or x==3 or x==4:
        if x==0:
            break

        #Função de cadstrar fornecedor
        elif x==1:
            nome = input("\nDigite o nome do Fornecedor: ")
            cnpj = input("\nDigite o cnpj do Fornecedor: ")
            telefone = input("\nDigite o telefone do Fornecedor")
            endereco = input("Digite o endereco do Fornecedor: ")
            f = Fornecedor(nome, cnpj, telefone, endereco)
            vf.addProduto(f)
    
        elif x==2:
            x = int(input("\nSe você quiser buscar: \nPor nome digite 1 \nPor código digite 2"))
            while x!=1 and x!=2:
                print("Digite um valor válido\n")
                x = int(input("\nSe você quiser buscar: \nPor nome digite 1 \nPor código digite 2"))
                if x==1:
                    nome = input("Digite o nome do Fornecedor")
                    vf.buscarFornecedorNome(nome)
                elif x==2:
                        cnpj = input("Digite o código do Fornecedor\n")
                        vf.buscarFornecedorCnpj(cnpj)
        
        elif x==3:
            listaFornecedores()
            
        elif x==4:
            removerFornecedorCnpj(nome)
