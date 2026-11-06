#calcular desconto

def calcular_desconto(valor,desconto):
    valor_desconto= valor-(valor*desconto/100)
    return valor_desconto

def receber_numero (mensagem):
    start=True
    while start:
        try:
            numero=float(input(mensagem).replace(",","."))
            start=False
        except:
            print("Valor invalido! Por favor, digite apenas numeros.")
        return numero


valor = receber_numero("Digite o valor do produto: ")
desconto = receber_numero("Digite o valor do desconto: ")

resultado = calcular_desconto(valor,desconto)
print("O valor do produto é: ",valor)       
print("O valor do desconto é: ",desconto,"%")
print("O valor do produto com desconto é: ",resultado)  