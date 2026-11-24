import mod_inputs
import mod_msg


def receber_opcao():
    while True:
        mod_msg.msg_valida_aeroporto()
        opcao = mod_inputs. recebe_int("Digite a opcao desejada: ")
        if opcao in(0,1,2,3,4,5):
            break
        else:
            print("Opção invalida!!\n")
        return opcao



def escolhe_aeroporto():
    aeroporto
    


        

     
def main():
    start = True
    while start:
        opcao = receber_opcao()
        if opcao != 0
            aeroporto= escolhe_aeroporto (opcao)
            distancia= escolhe_distancia (opcao)

          #start = mod_finaliza.finaliza_programa()
          

if __name__ == "__main__":
    main()
