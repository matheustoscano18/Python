from random import randint

cont = 0
pc = randint(0, 10)
acertou = False

print("Sou seu computador...\n"
      "Acabei de pensar em um número de 0 a 10.\n"
      "Será que você consegue adivinhar qual foi? ")

while not acertou:
    jogador = int(input("Qual é seu palpite? "))
    cont += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print("Mais... tente mais uma vez...")
        if jogador > pc:
            print("Menos... tente mais uma vez...")

print(f"Acertou com {cont} palpites!")
