
def soma (num1, num2):
    soma = num1 + num2
    return soma

def recebe_numero(mensagem):
    while True:
        try:
            num1=float(input(mensagem).replace(",","."))
            break
        except:
            print("Valor invalido!Por Favor, digite apenas o numeros.")
    return num1

num1 = recebe_numero("Digite o primeiro numero:")
num2 = recebe_numero("Digite o segundo numero:")

resultado = soma(num1,num2)
print("O resultado da soma é: ",resultado)

