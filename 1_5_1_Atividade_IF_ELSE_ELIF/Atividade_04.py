#Estrutura IF,Else e Elif

#Temperatura

try:
    temperatura = float(input("Digite a temperatura em Celsius: ").replace(",", "."))
    if temperatura<0:
        print ("A temperatura está em estado de congelamento é ", temperatura, "°C")

    elif temperatura>0 and temperatura<15:
        print ("A temperatura está em estado de frio é ", temperatura, "°C")

    elif temperatura>15 and temperatura<30:
        print ("A temperatura está em estado agradável é ", temperatura, "°C")


    else:
      print ("A temperatura está muito quente", temperatura, "°C")

except:
    print ("valor invalido, começe novamente")
