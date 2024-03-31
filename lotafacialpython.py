from time import sleep
from random import randint
from random import choice

def opcao_1():
    print("opção 1 escolhida.")
     # gerando um número aleatório entre 0 e 100
    esc2 = randint(1, 100)

    try:
        # usuário insere um número
        esc = int(input("Digite um número entre 0 e 100: "))
        # comparando os números
        if (esc < 0 or esc > 100):
            return print("Número inválido. Digite um número entre 0 e 100.")
        elif (esc == esc2):
            return print("Parabéns, você ganho R$ 1.000,00 reais")
        else:
            return print(f"Que pena! O número sorteado foi {esc2}")
    except ValueError:
        print("Valor inválido. Digite um número na próxima vez!")

def opcao_2():
    print("opção 2 escolhida.")
    # sorteando uma letra de A até Z
    sort = choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    
    try:
        # Usuário escolhe uma letra e converte para maiúscula
        letr_usu = str(input("Digite um letra de A até Z: ")).upper()
        if (sort == letr_usu):
            print(F"Parabéns. Você ganhou! A letra sorteada foi {sort}")
        else:
            print(f"Você perdeu. A letra sorteada foi {sort}")
    except ValueError:
        print("Valor inválido. Digite uma letra da próxima vez!")    


def opcao_3():
    print("Opção 3 escolhida")
    # gerando um número aleatório 
    esc2 = randint(0, 10)
    # usuário escolhe entre par e impar
    print("1 para postar em PAR")
    print("2 para apostar em IMPAR")
    try:
        # lendo a escolha do usuário
        esc = int(input("Escolha a opção desejada: "))
        if (esc == 1 and esc2 % 2 == 0):
            print("Parabéns! Você ganhou R$10,00 ")
            print(f"O número sorteado foi {esc2}")
            sleep(0.5)
        elif (esc == 2 and esc2 % 2 != 0):
            print("Parabéns. Você ganhou R$10,00")
            print(f"O número sorteado foi {esc2}")
            sleep(0.5)
        elif (esc < 1 and esc > 2):
            print("Opçãp inválida. Escolhe dentre as opções informadas na próxima vez!")
        else:
            print("Que pena. Você perdeu!")
            print(f"O número sorteado foi {esc2}")
            sleep(0.5)
    except ValueError:
        print("Valor inválido. Escolha uma das opções informadas na próxima vez!")


escolha = 1

while escolha != 0:
    print("*************************************")
    print("Menu loteria")
    print("1: Apostar de 0 a 100")
    print("2: Apostar em uma letra de A a Z")
    print("3: apostar entre impar e par")
    print("*************************************")
    sleep(0.5)

    try:
        escolha = int(input("Escolha a modalidade desejada (ou digite 0 para sair): "))
        
        if escolha == 1:
            resultado = opcao_1()
        elif escolha == 2:
            resultado = opcao_2()
        elif escolha == 3:
            resultado = opcao_3()
        elif escolha == 0:
            print("Saindo...")
        else:
            print("Opção inválida! Escolha uma opção válida.")
    except ValueError:
        print("Entrada inválida! Por favor, digite um número.")

    sleep(0.5)