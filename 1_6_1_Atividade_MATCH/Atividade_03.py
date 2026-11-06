#menu bancario

try:
    print("Digite um dos números a seguir: \n")
    print("Para Consultar Saldo digite:1")
    print("Para Depositar digite:2")
    print("Para Sacar digite:3")
    print("Para Sair digite:4")

    num=str(input("Digite um número acima:"))
    match num:
        case"1":
            print("Para 1 digite: Consultar Saldo")
            print("Saldo atual: R$ 1000,00")


        case"2":
            print("Para 2 digite: Depositar")
        case"3":
            print("Para 3 digite: Sacar")
        case"4":
            print("Para 4 digite: Sair")
        case _:
            print("Número inválido!")
except:
    print ("número digitado é inválido!")
