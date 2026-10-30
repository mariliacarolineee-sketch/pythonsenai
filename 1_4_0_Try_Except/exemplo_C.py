try:
    num1 = float(input("Digite um número:").replace(",","."))
    num2 = float(input("Digite um numero:").replace(",","."))
    resultado = num1/num2
    print("o valor da divisão é", num1/num2)   
except ValueError:
    print("Valor invalido!Não foi possivel realizar o calculo.")
except ZeroDivisionError:
       print("Erro! Não é possivel dividir um numero por zero.")