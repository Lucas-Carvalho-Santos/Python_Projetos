from time import sleep
from random import randint

# VARIÁVEIS UTILIZADAS AO LONDO DO PROGRAMA
PortaEscolhida = 0
PortaSorteada = 0
PortaVazia = 0 
NovaPortaEscolhida = 0


print("Bem vindo ao jogo Monty Hall")

#USUÁRIO ESCOLHE A PORTA 
while (PortaEscolhida < 1 or PortaEscolhida > 3):
    try:
        PortaEscolhida = int(input('Escolha uma das portas: 1, 2 ou 3 para jogar: '))
        sleep(0.5)
    except ValueError:
        print('Opção inválida. Escolha entre as opções oferecidas.')
        sleep(0.5)

# MOSTRANDO A PORTA ESCOLHIDA
print(f'Você escolheu a porta {PortaEscolhida}')

#SORTEANDO UMA PORTA 
PortaSorteada = randint(1, 3)

# ESCOLHENDO UMA PORTA VAZIA
while (PortaVazia == PortaEscolhida or PortaVazia == PortaSorteada or PortaVazia == 0):
    PortaVazia = randint(1, 3)
    if (PortaVazia != PortaEscolhida and PortaVazia != PortaSorteada):
        break

# MOSTRANDO UMA DAS PORTAS VAZIAS
print(f'A porta {PortaVazia} está vazia')

# USUÁRIO ESCOLHE SE DESEJA TROCAR DE PORTA
resposta = input('Deseja troca de porta? [s/n]').upper()

if (resposta == 'S'):
    while (NovaPortaEscolhida == PortaEscolhida or NovaPortaEscolhida  == PortaSorteada or NovaPortaEscolhida  == 0):
        NovaPortaEscolhida  = randint(1, 3)
        if (NovaPortaEscolhida != PortaEscolhida and NovaPortaEscolhida  != PortaVazia):
            print(f'NOVA PORTA ESCOLHIDA: {NovaPortaEscolhida}')
            # TESTANDO SE A NOVA PORTA É A PORTA SORTEADA
            if (NovaPortaEscolhida == PortaSorteada):
                print('Parabéns! Você escolher a porta sorteda!')
            else:
                print(f'Você perdeu! A porta sorteada foi {PortaSorteada}')
            break
else:
    print(f'Você continuou com a porta {PortaEscolhida}')
    # TESTANDO SE A PRIMEIRA PORTA ESCOLHIDA É PORTA SORTEADA
    if (PortaEscolhida == PortaSorteada):
        print('Parabéns! Você escolher a porta sorteda!')
    else:
        print(f'Você perdeu! A porta sorteada foi {PortaSorteada}')