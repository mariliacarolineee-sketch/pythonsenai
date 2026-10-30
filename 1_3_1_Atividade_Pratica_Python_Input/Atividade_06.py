#Recebendo Dados do Input

#Receber os dados
num1 = float(input ("Digite no 1º: ").replace(",", "."))
num2 = float(input ("Digite no 2º: ").replace(",", "."))

#processar variaveis 
soma= num1 + num2
resultado = ((soma) **(1/2))

#visualizar os dados
print("o valor da raiz quadrada de" , soma, "é igual a", resultado)
