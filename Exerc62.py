# ismail ahmad kanabawi
lista = []
cont = 0
while True:
    num = int(input("Digite um valor: "))
    if cont == 0:
        lista.append(num)
        print("Valor adicionado com sucesso...")
    if cont > 0 and num in lista:
        print("Valor duplicado! Não vou adicionar...")
    elif cont > 0 and num not in lista:
        lista.append(num)
        print("Valor adicionado com sucesso...")
    escolha = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if escolha not in 'SN':
        escolha = str(input("Quer continuar? [S/N] "))
    if escolha == 'N':
        break
    cont += 1
print("-=" * 30)
print(f"Você digitou os valores {sorted(lista)}")
