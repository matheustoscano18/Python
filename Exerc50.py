n1 = int(input("Digite um número para calcular seu fatorial: "))
cont = n1
f = 1
print(f"Calculando {n1}! = ", end='')
while cont > 0:
    print(f"{cont}", end='')
    print(f" x " if cont > 1 else " = ", end='')
    f *= cont
    cont -= 1
print(f"{f}")
