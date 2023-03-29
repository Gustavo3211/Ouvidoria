#Sistema de ocorrencias
#Gustavo Pires de Carvalho
#Cadastrar, Listar, Apagar, Sair 
#operações com o banco de dados


# FUNÇÕES DO MENU:
import classes_mysql as CB 

def cadastrar_ocorrencia():
    print("")
    print("")
    print("Cadastro de ocorrência")
    print("")
    print("digite 'sair' para sair")
    print("")
    ocorrencia = str(input("Digite sua ocorrência: "))
    if ocorrencia == "" or ocorrencia == "sair":
        print("voltando...")
        menu()

    print("1- Elogio")
    print("2- Reclamação")
    print("3- Sugestão")
    tipo = input("Que tipo de ocorrencia é essa?:")
    try:
        tipo = int(tipo)
    except:
        print("tipo inválido!")
        print("use apenas numeros inteiros.")
        cadastrar_ocorrencia()
    

    if tipo <= 3 and tipo >= 1:

        CB.inserirbanco(cnx,ocorrencia,tipo)
    else:
        print("tipo inválido!")
        print("use apenas numeros inteiros.")


''' lista_ocorrencias.append(ocorrencia)
    print("Ocorrência cadastrada com sucesso")'''

def apagar_ocorrencias():
    print("----------")
    print("")
    print("")
    print("Deletar ocorrencias")
    print("")
    print("1- Apagar uma ocorrência específica")
    print("")
    print("2- Apagar todas as ocorrências")
    print("")
    print("0- para voltar")
    print("")
    opcao = int(input("Digite uma opção: "))

    #APAGAR TODAS AS OCORRENCIAS
    if opcao == 2:
        print("você tem certeza? este é um processo IRREVERSSIVEL! tenha certeza de ter um backup destes dados, deseja continuar? digite sim ou nao")
        print("")
        opcao = input("Digite uma opção: ")   
        if opcao == "sim" or opcao == "SIM":
            CB.truncate(cnx)

        else:
            apagar_ocorrencias()

    #APAGAR APENAS UMA OCORRENCIA.
    if opcao == 1:
        CB.listarbanco(cnx)
        print("")
        print("para voltar digite 'sair'")
        ocorrencia = input("Digite o Numero da ocorrencia: ")
        if ocorrencia == "sair":
            menu()
        else:
        
            try:
                ocorrencia = int(ocorrencia)
            except ValueError:
                print("Valor Inválido! insira apenas NUMEROS!")
        
        CB.deletabanco(cnx,ocorrencia)
    if opcao == 0:
        print("Voltando...")
        menu()



def pesquisar():
    print("Pesquisar ocorrencia")
    print("")
    print("1- Elogio")
    print("2- Reclamação")
    print("3- Sugestão")
    tipo = input("Que tipo de ocorrencia você quer pesquisar?:")
    if tipo != "sair":
        try:
            tipo=int(tipo)
            CB.pesquisarbanco(cnx,tipo)
        except ValueError:
            print("Valor inválido! insira um numero inteiro.")
            pesquisar()
        except:
            print("Esta ocorrencia não existe!")
            pesquisar()
    else:
        print("Voltando...")
        menu()


# ----------------------------

def menu():
    print("----")
    print("MENU")
    print("")
    print("1- Cadastrar ocorrência")
    print("2- Lista de todas as ocorrências")
    print("3- Apagar ocorrência")
    print("4- Pesquisar ocorrencia")
    print("5- Sair do sistema")

    print("")
    opcao = 0
    try:
        opcao = int(input("Digite a opção desejada: "))
        
    except ValueError:
        print("Digite uma opção válida!")
        menu()
    print("")
    if opcao == 1:
        cadastrar_ocorrencia()
    elif opcao == 2:
        CB.listarbanco(cnx)
    elif opcao == 3:
        apagar_ocorrencias()
    elif opcao == 4:
        pesquisar()
    elif opcao == 5:
        print("")
        print("Saindo do sistema...")
        print("")
        CB.desligarbanco(cnx)
        exit()
    else:
        print("Digite uma opção válida")
    print("")   



cnx = CB.conectar()
while True:

    menu()
    