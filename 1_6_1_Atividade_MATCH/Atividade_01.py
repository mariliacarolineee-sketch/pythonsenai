#criação de calculadora


try:
    num1=float(input("Digite o primeiro número: ").replace(",", "."))
except:
    print ("valor inválido para o primeiro número!")


try:       
    num2=float(input("Digite o segundo número: ").replace(",", "."))
except:
    print ("valor inválido para o segundo número!") 


try:
    print("Digite uma das operações a seguir: \n")
    print("Para multiplicação digite: *")
    print("Para divisão digite: /")
    print("Para adição digite: + ")
    print ("Para subtração digite:-")

    operador = str(input("Digite o operadoração acima: "))
except:
    print ("operador digitado é inválido!") 

match operador:
    case"*":
        resultado = num1*num2
        print(num1,operador, num2,"é = ", resultado)
    case"/":
        resultado= num1/num2
        print(num1,operador, num2,"é=", resultado)
    case"+":
        resultado=num1+num2
        print(num1,operador, num2,"é=", resultado)
    case"-":
        resultado=num1-num2
        print(num1,operador,num2,"é=",resultado)
    case _:
        print("operador digitado é inválido!")