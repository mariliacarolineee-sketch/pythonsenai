senha = 0

while senha != 1234:
    try:
        senha=int(input("Digite a senha: "))
    except:
        print("Valor inválido, digite apenas números.\n")

print("\n Senha correta, acesso permitido.")


