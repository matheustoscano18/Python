print("=" * 30)
print("\t\t  BANCO CEV")
print("=" * 30)

saque = int(input("Quanto você quer sacar? R$"))
valor = saque
ced = 50
cedqnt = 0

while True:
    if valor >= ced:
        valor -= ced
        cedqnt += 1
    else:
        if cedqnt > 0:
            print(f"Total de {cedqnt} cédulas de R${ced}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        cedqnt = 0
        if valor == 0:
            break

print("=" * 30)
print("Volte sempre ao banco CEV!")
