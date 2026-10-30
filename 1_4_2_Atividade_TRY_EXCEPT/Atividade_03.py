try:
    numero=float(input ("Digite o preço do produto:").replace(',', '.'))
    desconto=float(input("Digite o desconto do produto:").replace(',', '.')) 
    resultado=numero-(numero*desconto/100)
    print("O preço do produto com desconto é:",resultado)
except:
    print("Valores inválidos, tente novamente.")