lista = []
pares = []
impares = []
while True:
    num = int(input("Digite um número: "))
    lista.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    escolha = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if escolha == 'N':
        break
print("-=" * 20)
print(f"A lista completa é {lista}")
print(f"A lista de pares é {pares}")
print(f"A lista de impares é {impares}")
