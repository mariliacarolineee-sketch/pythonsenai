#Estrutura IF,Else e Elif

#Nota do Aluno


try:
    nota=float(input("Digite a nota do aluno:").replace(",","."))

    if nota<0 or nota>10.00:
       print ("nota invalida, digite novamente")
    elif nota >=0 and nota <=4.90:
        print ("Aluno está reprovado")
    elif nota >=5.00 and nota <=6.90:
        print ("Aluno em recuperação")
    elif nota >=7.00 and nota <=10.00:
        print ("Aluno está aprovado")
    
except:
    print ("nota invalida, começe novamente")