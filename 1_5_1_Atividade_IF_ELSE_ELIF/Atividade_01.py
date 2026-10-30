#Estrutura IF,Else e Elif

try:
    idade= int(input("Digite sua idade: "))
    if idade <=0:
        print("idade inválida")
    elif idade <= 12:
        print("Você é uma criança")
    elif idade >=13 and idade <=17:
        print("Você é um adolescente")
    else:
        print("Você ja é um adulto")

except:
    print ("idade invalida, digite novamente")
