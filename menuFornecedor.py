from Fornecedores import Fornecedor
from vetorFornecedor import vetorFornecedor

class menuFornecedor:
    def menuF(vf):
        x = int(input("Digite: \n0 Para sair \n1 Para cadastrar Fornecedor \n2 Buscar Fornecedor \n3 Para listar Fornecedores \n4 Remover Fornecedores\n"))
        while x!=0 and x!=1 and x!=2 and x!=3 and x!=4:
            print("Digite um valor válido\n")
            x = int(input("Digite: \n0 Para sair \n1 Para cadastrar Fornecedor \n2 Buscar Fornecedor \n3 Para listar Fornecedores \n4 Remover Fornecedores\n"))
        
        while x==0 or x==1 or x==2 or x==3 or x==4:
            if x==0:
                return
            #Função de cadstrar fornecedor
            elif x==1:
                nome = input("Digite o nome do Fornecedor: ")
                cnpj = int(input("Digite o cnpj do Fornecedor: "))
                telefone = input("Digite o telefone do Fornecedor: ")
                endereco = input("Digite o endereco do Fornecedor: ")
                f = Fornecedor(nome, cnpj, telefone, endereco)
                vf.addFornecedor(f)
        
            elif x==2:
                x = int(input("\nSe você quiser buscar: \nPor nome digite 1 \nPor código digite 2 "))
                while x!=1 and x!=2:
                    print("Digite um valor válido\n")
                    x = int(input("\nSe você quiser buscar: \nPor nome digite 1 \nPor código digite 2 "))
                if x==1:
                    nome = input("Digite o nome do Fornecedor: ")
                    vf.buscarFornecedorNome(nome)
                elif x==2:
                    cnpj = int(input("Digite o cnpj do Fornecedor: "))
                    vf.buscarFornecedorCnpj(cnpj)
            
            elif x==3:
                vf.listaFornecedores()
                
            elif x==4:
                cnpj = int(input("Digite o cnpj do fornecedor: "))
                vf.removerFornecedorCnpj(cnpj)

            x = int(input("Digite: \n0 Para sair \n1 Para cadastrar Fornecedor \n2 Buscar Fornecedor \n3 Para listar Fornecedores \n4 Remover Fornecedores\n"))

