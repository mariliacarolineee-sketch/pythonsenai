
#verificar se o numero é par ou impar

def verificar_numero():
    while True:
        try:
            return int(input("Digite um numero inteiro: "))
        except ValueError:
            print("Valor invalido! Digite um numero inteiro.")


numero = verificar_numero()
if numero % 2 == 0:
    print("O numero é par")
else:
    print("O numero é impar")
