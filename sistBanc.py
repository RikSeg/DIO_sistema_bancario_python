
menu = """
[SISTEMA DE BANCO]

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
depoStr = "- Deposito: R$"
saqueStr = "- Saque: R$" 
extratoStr = ""
numero_saques = 0
LIMITE_SAQUES = 3

def funcDeposito():
    global saldo 
    global extratoStr
    global depoStr
    depo = input("Valor do depósito: R$")
    saldo += float(depo)
    extratoStr += depoStr + depo + "\n"
    print("[DEPOSITO EXECUTADO COM SUCESSO]")

def funcSaque():
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



def funcExtrato():
    global extratoStr
    if(extratoStr is ""):
        print("[NÃO FORAM EFETUADAS TRANSAÇÕES]")
    else:    
        print(extratoStr)
        print("Total: R${:.{}f}".format(saldo,2))

while True:

    opcao = input(menu)

    if opcao == "d":
        print("\n[DEPÓSITO]")
        deposito()

    elif opcao == "s":
        print("\n[SAQUE]")
        saque()
    elif opcao == "e":
        print("\n[EXTRATO]")
        extrato()
    elif opcao == "q":
        print("\nSaindo...")
        break