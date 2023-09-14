print("Gerador de PA")
print("-=" * 10)
p1 = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))
termo = p1
cont = 1
while cont <= 10:
    print(f"{termo} -> ", end='')
    termo += razao
    cont += 1
print("Acabou!")
