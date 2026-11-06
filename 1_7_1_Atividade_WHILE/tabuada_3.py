inicio = True

while inicio:

    try:
        numero = int(input("Digite um número para ver sua tabuada:"))
       
        inicio = False
    
    except:
        print("Por favor, digite um número válido.")
        
   
contador = 1

while contador <= 10:
    print(numero, "x", contador, "=", numero * contador)
    contador+=1


