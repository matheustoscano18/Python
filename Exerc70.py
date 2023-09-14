matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = colsoma = mai = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f"Digite um valor para [{linha}] [{coluna}]: "))
print("-=" * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f"[{matriz[linha][coluna]:^5}]", end='')
        if matriz[linha][coluna] % 2 == 0:
            soma += matriz[linha][coluna]
    print()
print("-=" * 30)
print(f"A soma dos valores pares é {soma}.")
for linha in range(0, 3):
    colsoma += matriz[linha][2]
print(f"A soma dos valores da terceira coluna é de {colsoma}.")
for coluna in range(0, 3):
    mai = max(matriz[1])
print(f"O maior valor da segunda linha é {mai}.")
