#Recebendo Dados usando o input

#Receber o nome do usuario:
nome = str(input ("Digite seu nome completo:"))

#Receber a idade do usuario:
idade = int(input ("Digite sua idade em anos:"))

#Receber a peso do usuario:
peso = float(input ("Informe seu peso em Kg:").replace(",", "."))


#Visualizar o nome digitado
print ("O nome do usuario é: ", nome)
print ("A idade do usuario é: ", idade, "anos")
print ("O peso do usuario é: ", peso, "kg")

