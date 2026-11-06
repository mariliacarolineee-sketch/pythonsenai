#calcular nota de aluno

def calcular_nota(nota1,nota2,nota3):
    media = (nota1+nota2+nota3)/3
    return media

def receber_numero (mensagem):
    start=True
    while start:
        try:
            numero=float(input(mensagem).replace(",","."))
            start=False
        except:
            print("Valor invalido! Por favor, digite apenas numeros.")


    return numero

nota1 = receber_numero("Digite o primeiro nota:")
nota2 = receber_numero("Digite o segundo nota:")
nota3 = receber_numero("Digite o terceira nota:")

resultado = calcular_nota(nota1,nota2,nota3)
print("o resultado da média é: ",resultado)


if resultado >=7:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")