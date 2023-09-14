print("===" * 10)
print("\t10 TERMOS DE UMA PA")
print("===" * 10)

p1 = int(input("Primeiro termo: "))
r = int(input("Razão: "))
cont = p1 + (10 - 1) * r
for c in range(p1, cont + r, r):
    print(c, end=' -> ')
print("ACABOU")
