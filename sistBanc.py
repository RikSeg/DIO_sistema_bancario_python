#VARIÁVEIS GLOBAIS
menu = """
[SISTEMA BANCÁRIO]

[1] Cadastrar usuário
[2] Lista usuários
[3] Cadastrar conta
[4] Depositar
[5] Sacar
[6] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
depoStr = "- Deposito: R$"
saqueStr = "- Saque: R$" 
extratoStr = ""
numero_saques = 0
LIMITE_SAQUES = 3

usuarios = []
contas = []
numero_contas = 0
##

#Funções de operações
def funcdeposito():
    global saldo 
    global extratoStr
    global depoStr
    depo = input("Valor do depósito: R$")
    saldo += float(depo)
    extratoStr += depoStr + depo + "\n"
    print("[DEPOSITO EXECUTADO COM SUCESSO]")

def funcsaque():
    global saldo
    global extratoStr
    global LIMITE_SAQUES
    global numero_saques
    if(saldo == 0):
        print("[SALDO INSUFICIENTE PARA SAQUE]")
    elif(numero_saques == LIMITE_SAQUES):
        print("[LIMITE DE SAQUES ATINGIDO - 3]")
    else:
        print("Número de Saques possíveis:" + str(numero_saques) + "/3")
        saque = input("Valor do saque: R$")
        if float(saque) > 500:
            print("[VALOR ACIMA DO LIMITE, TRANSAÇÃO CANCELADA]")
        
        else:
            saldo -= float(saque)
            extratoStr += saqueStr + saque + "\n"
            numero_saques +=1
            print("[SAQUE EXECUTADO COM SUCESSO]")


def funcextrato():
    global extratoStr
    if(extratoStr == ""):
        print("[NÃO FORAM EFETUADAS TRANSAÇÕES]")
    else:    
        print(extratoStr)
        print("Total: R${:.{}f}".format(saldo,2))
##

#funções de cadastro
def cadastraCliente():
    global usuarios
    auxlist =[]
    print("Insira os dados do cliente:")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    logradouro = input("Logradouro: ")
    nro = input("Nro: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    estado = input("Estado(sigla): ")
    endereco = logradouro + "," + nro + " - " + bairro + " - " + cidade + "/" + estado.upper()
    auxlist.append(nome)
    auxlist.append(cpf)
    auxlist.append(endereco)
    usuarios.append(auxlist)
    return 0

def criaConta():
    global contas
    global numero_contas


    return 0
##

#função para listar clientes
def listaClientes():
    global usuarios
    if len(usuarios) == 0 :
        print("[SEM USUÁRIOS CADASTRADOS]")
    else:
        print("[LISTA DE USUÁRIOS] \n[nome;cpf;endereço]")
        for u in usuarios:
            count +=1
            print(count +"- " + u[0] + "; " + u[1] + "; " + u[2])

#Função principal
def main():
    #Seletor de opções
    while True:

        opcao = input(menu)
        if opcao == "1":
            print("\n[CADASTRO DE USUÁRIO]")
            cadastraCliente()
        elif opcao == "2":
            print("\n[LISTA USUÁRIOS]")
            listaClientes()
        elif opcao == "3":
            print("\n[CADASTRO DE CONTA]")
            criaConta()
        elif opcao == "4":
            print("\n[DEPÓSITO]")
            funcdeposito()

        elif opcao == "5":
            print("\n[SAQUE]")
            funcsaque()
        elif opcao == "6":
            print("\n[EXTRATO]")
            funcextrato()
        elif opcao == "0":
            print("\nSaindo...")
            break
##

#execução da função principal
main()