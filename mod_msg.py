import pyfiglet

def msg_inicial():
    print ("Seja Bem Vindo ao Sistema\n")
    mensagem = pyfiglet.figlet_format ("Cota Frete", font="pagga")
    print(mensagem)


def msg_login_ini():
    print("#############################################################")
    print("<<<<<<<<<<<<<<<<<<<<< LOGAR NO SISTEMA >>>>>>>>>>>>>>>>>>>>>>")

def msg_menu_principal():
    print("##########################################################")
    print("<<<<<<<<<<<<<<<<<<<< MENU PRINCIPAL >>>>>>>>>>>>>>>>>>>>>>")
    print("##########################################################\n")
    print("##### SAIR - 0 | CALCULADORA - 1 | CALCULA FRETE - 2 #####\n")

def msg_calc_ini():
    print("##############################")
    print("<<<<<<<< CALCULADORA >>>>>>>>>")
    print("##############################\n")


def msg_valida_aeroporto():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Escolha o Destino~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("0 - Sair")
    print("1 - Congonhas/SP") 
    print("2 - Guarulhos/SP")
    print("3 - Campo de Marte/SP")  
    print("4 - Pinto Martins/CE")
    print("5 - Eduardo Gomes/AM ") 

def msg_final_programa():
    print("#############################################################################")
    print("<<<<<<<<<<<<Obrigada por utilizar o programa cota-frete>>>>>>>>>>>>>>>>>>>>>>")
    print("######################################### Volte Sempre!!!!!################\n")