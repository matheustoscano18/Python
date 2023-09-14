princ = [[], []]
for c in range(1, 8):
    num = int(input(f"Digite o {c}o. valor: "))
    if num % 2 == 0:
        princ[0].append(num)
    else:
        princ[1].append(num)
princ[0].sort()
princ[1].sort()
print("-=" * 30)
print(f"Os valores pares digitados foram: {princ[0]}")
print(f"Os valores ìmpares digitados foram: {princ[1]}")
