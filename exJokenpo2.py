from time import sleep
from random import randint

itens = ('PEDRA', 'PAPEL', 'TESOURA')
pc = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
player = int(input("Qual é a sua jogada? "))

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
print("-=" * 14)

print(f"Computador escolheu {itens[pc]}")
print(f"O jogador escolheu {itens[player]}")
print("-=" * 14)

if pc == 0:  # computador jogou PEDRA
    if player == 0:
        print('EMPATE')
    elif player == 1:
        print('JOGADOR VENCE')
    elif player == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVALIDA')

elif pc == 1:  # computador jogou PAPEL
    if player == 0:
        print('COMPUTADOR VENCE')
    elif player == 1:
        print('EMPATE')
    elif player == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVALIDA')

elif pc == 2:  # computador jogou TESOURA
    if player == 0:
        print('JOGADOR VENCE')
    elif player == 1:
        print('COMPUTADOR VENCE')
    elif player == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')
