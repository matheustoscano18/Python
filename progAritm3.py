print("Gerador de PA")
print("-=" * 10)
p1 = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))
termo = p1
cont = 1
tot = 0
mais = 10
while mais != 0:
    tot += mais
    while cont <= tot:
        print(f"{termo} -> ", end='')
        termo += razao
        cont += 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais? "))
print("FIM")
