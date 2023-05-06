from defs import *

limpar_tela()
saudacao()

nome_do_usuario = input("Qual seu nome? ").capitalize()

limpar_tela()

print(f"Olá {nome_do_usuario}, bem vindo o meu Quiz.\n\nVou te fazer algumas perguntas sobre python.\nPontuação Maxima: 6\nEspero que se divirta <3\n")

proxima_questão()
input()

comecar_jogar = int(input("Vamos comecar a jogar? \"1\" pra \"sim\" e \"2\" pra \"não\": "))
limpar_tela()

print("Ok vamos lá <3")
proxima_questão()
limpar_tela()

if comecar_jogar == 1:

    pontos = 0

    #Questão 1
    print("1. Qual é a função do comando \"print\" em Python?\n")
    print("(a) O comando \"print\' em Python é usado para exibir informações na tela do usuário.")
    print("(b) O comando \"print\" em Python é usado para receber entrada do usuário.")
    pergunta_1 = input("RESPOSTA: ").lower()

    limpar_tela()

    if pergunta_1 == "a":
        pontos = pontos + 1
        print("Você acertou!")
    else:
        print("Você errou </3")

    proxima_questão()

    input()
    limpar_tela()

    #Questão 2
    print("2. Como você define uma variável em Python?\n")
    print("(a)Para definir uma variável em Python, você precisa usar a palavra-chave \"set\" seguida pelo nome da variável. Por exemplo: set nome = \"João\"")
    print("(b) Para definir uma variável em Python, você precisa escolher um nome para ela e atribuir um valor a esse nome, usando o sinal de igual (=). Por exemplo: nome = \"João\"")
    pergunta_2 = input("RESPOSTA: ").lower()

    limpar_tela()

    if pergunta_2 == "b":
        pontos = pontos + 1
        print("Você acertou!")
    else:
        print("Você errou </3")
    
    proxima_questão()

    input()
    limpar_tela()

    #Questão 3
    print("3. O que é uma lista em Python?\n")
    print("(a) Em Python, uma lista é uma estrutura de dados que permite armazenar uma coleção ordenada de elementos.")
    print("(b) Em Python, uma lista é uma estrutura de dados que permite armazenar apenas números inteiros.")
    pergunta_3 = input("RESPOSTA: ").lower()

    limpar_tela()

    if pergunta_3 == "a":
        pontos += 1 
        print("Você acertou!")
    else:
        print("Você errou </3")

    proxima_questão()

    input()
    limpar_tela()

    print("Agora as coisas vão esquantar!\n")

    proxima_questão()

    input()
    limpar_tela()

    #Questão 4
    print("4. Qual é a diferença entre uma tupla e uma lista em Python?\n")
    print("(a) A diferença entre uma tupla e uma lista em Python é que uma tupla pode ter um número variável de elementos, enquanto uma lista tem sempre um tamanho fixo.")
    print("(b) A diferença entre uma tupla e uma lista em Python é que uma tupla é imutável, enquanto uma lista é mutável.")
    pergunta_4 = input("RESPOSTA: ").lower()


    limpar_tela()

    if pergunta_4 == "b":
        pontos += 1
        print("Você acertou!")
    else:
        print("Você errou </3")

    proxima_questão()

    input()
    limpar_tela()
    
    #Questão 5

    print("5. Explique a diferença entre uma classe e um objeto em Python.\n")
    print("(a) Em Python, uma classe é uma definição de um objeto, enquanto um objeto é uma instância de uma classe.")
    print("(b) Em Python, uma classe é um objeto que encapsula apenas funções, enquanto um objeto é uma variável que contém apenas dados.")
    pergunta_5 = input("RESPOSTA: ").lower()

    limpar_tela()

    if pergunta_5 == "a":
        pontos += 1
        print("Você acertou!")
    else:
        print("Você errou </3")

    proxima_questão()

    input()
    limpar_tela()

    #Questão 6

    print("6. O que são os métodos de string em Python?\n")
    print("(a) Os métodos de string em Python são funções que podem ser aplicadas a strings para modificar ou obter informações sobre elas. Alguns exemplos de métodos de string são: .lower(), .upper(), .replace().")
    print("(b) Os métodos de string em Python são funções especiais que podem ser usadas somente em strings literais e não em variáveis.")
    pergunta_6 = input("RESPOSTA: ").lower()


    limpar_tela()

    if pergunta_6 == "a":
        pontos += 1
        print("Você acertou!")
    else:
        print("Você errou </3")

    print("FIM DE JOGO!")

    input()
    limpar_tela()

    print("Sua pontuação foi de",pontos,"/ 6")

    if pontos == 0 or pontos == 1 or pontos == 2:
        print("Você no foi muito bem...MAS vc pode jogar novamente ;)\n")
        proxima_questão()

    if pontos == 3 or pontos == 4:
        print("Vc foi bem. Mas pode melhorar <3\n")
        proxima_questão()

    if pontos == 5:
        print("Parabéns. Aposto qu da proxima você zera a jogo <3 <3\n")
        proxima_questão()

    if pontos == 6:
        print("Você ZEROU o jogo. PARABÉNS <3\n")
        proxima_questão()
else:
    print("Você escolheu sair.")
    exit()