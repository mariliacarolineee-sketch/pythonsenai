
def soma (num1, num2):
    soma = num1 + num2
    return soma

start=True

while start:
    try:
        num1=float(input("Digite o primeiro numero: ").replace(",","."))
        start=False
    except:
        print("Valor invalido! Por favor, digite apenas numeros.")


start=True
while start:
    try:
        num2=float(input("Digite o segundo numero: ").replace(",","."))
        start=False
    except:
        print("Valor invalido! por favor, digite apenas numeros.")

resultado = soma(num1,num2)
print("O resultado da soma é: ",resultado)
            