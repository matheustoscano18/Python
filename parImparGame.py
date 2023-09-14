from random import randint
vit = 0
print("=-" * 15)
print("VAMOS JOGAR PAR OU ÌMPAR")
print("=-" * 15)
while True:
    num = int(input("Diga um valor: "))
    pc = randint(0, 10)
    soma = num + pc
    tipo = ' '
    while tipo not in "PI":
        tipo = str(input("Par ou ìmpar? [P/I] ")).strip().upper()[0]
    print("-" * 30)
    print(f"Você jogou {num} e o computador {pc}. Total de {soma} ", end='')
    print("deu PAR" if soma % 2 == 0 else "deu ÌMPAR")
    print("-" * 30)
    if tipo == "P":
        if soma % 2 == 0:
            print("Você VENCEU!")
            vit += 1
        else:
            print("Você PERDEU!")
            break
    elif tipo == "I":
        if soma % 2 == 0:
            print("Voce PERDEU!")
            break
        else:
            print("Voce VENCEU!")
            vit += 1
        print("Vamos jogar novamente...")
print("=-" * 15)
print(f"GAME OVER! Você venceu {vit} vezes.")
