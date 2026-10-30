try :
    Nome= str(input("Digite seu nome por favor:"))
    Idade = int(input("Digite sua idade por favor:"))
    print("Olá,",Nome,"seja bem-vindo(a)!")
    print("Sua idade é:", Idade," anos.")
except:
    print ("ocorreu um erro, tente novamente.")