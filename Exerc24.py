from random import randint
from time import sleep
# Jogo da adivinhação de 0 a 5
adiv = randint(0, 5)
print("-=-" * 20)
print("Vou pensar em um número de 0 a 5. Tente adivinhar...")
print("-=-" * 20)

num = int(input("Em que número pensei? "))

print("PROCESSANDO...")
sleep(3)

if num == adiv:
    print("PARABÉNS, VOCÊ GANHOU!")
else:
    print("ERROU! EU PENSEI NO {} E NÃO NO {}".format(adiv, num))
