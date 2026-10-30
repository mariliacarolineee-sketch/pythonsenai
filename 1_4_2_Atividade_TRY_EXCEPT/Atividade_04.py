try:
    nota1=float(input ("Digite a 1ª nota do aluno:").replace(',', '.'))
    nota2=float(input("Digite a 2ª nota do aluno:").replace(',', '.'))
    nota3=float(input("Digite a 3ª nota do aluno:").replace(',', '.')) 
    resultado=media=(nota1+nota2+nota3)/3

    if resultado>=7:
        print("O aluno está aprovado!")
    else:
        print("O aluno está reprovado!")
    
    print("A média do aluno é:",resultado)
    
    

except:
    print("Valores inválidos, tente novamente.")