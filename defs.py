#def de saudações

import os

def saudacao():
    print("Seja bem vindo ao meu programa <3")

def limpar_tela():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def proxima_questão():
    print("Aperte \"ENTER\" para continuar jogando...")

