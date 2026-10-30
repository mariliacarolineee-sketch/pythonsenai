#Estrutura IF,Else e Elif

#LOJA Descontos


try:
    valor=float(input("Digite o valor da compra:").replace(",","."))

    if valor <0:
       print ("valor invalido")

    elif valor <=100.00:
        print ("sem desconto")
        print ("o valor da compra é de R$",valor)

    elif valor >100 and valor <=500.00:
       vlr_desconto= valor *(1-(10/100))
       print ("desconto de 10%")
       print ("o valor da compra com desconto é de R$",vlr_desconto)

    elif valor >500.00:
        vlr_desconto= valor *(1-(15/100))       
        print ("desconto de 15%")
        print (" o valor da compra com desconto é de R$", vlr_desconto)
        
except:
    print ("valor invalido, começe novamente")