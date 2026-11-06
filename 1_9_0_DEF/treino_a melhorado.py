
def soma (num1, num2):
    soma = num1 + num2
    return soma

def receber_numero (mensagem):
    start=True
    while start:
        try:
            numero=float(input(mensagem).replace(",","."))
            start=False
        except:
            print("Valor invalido! Por favor, digite apenas numeros.")
    return numero

num1 = receber_numero("Digite o primeiro numero: ")
num2 = receber_numero("Digite o segundo numero:")

resultado = soma(num1,num2)
print("O resultado da soma é: ",resultado)


            