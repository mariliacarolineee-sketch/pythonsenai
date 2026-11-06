#informar o dia da semana correspondente


try:
    print("Digite um dos números a seguir: \n")
    print("Para 1 digite: Domingo")
    print("Para 2 digite: Segunda-feira")
    print("Para 3 digite: Terça-feira")
    print("Para 4 digite: Quarta-feira")
    print("Para 5 digite: Quinta-feira")
    print("Para 6 digite: Sexta-feira")
    print("Para 7 digite: Sábado")

    num = str(input("Escolha um número acima: "))
    match num:
        case"1":
            print("Domingo")
        case"2":
            print("Segunda-feira")
        case"3":
            print("Terça-feira")
        case"4":
            print("Quarta-feira")
        case"5":
            print("Quinta-feira")
        case"6":
            print("Sexta-feira")
        case"7":
            print("Sábado")
        case _:
            print("Número inválido!")
except:
    print ("número digitado é inválido!") 

  
