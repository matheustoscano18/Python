# Soma exclusiva de números PARES
cont = 0
quant = 0
for c in range(1, 7):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        quant = quant + 1
        cont = cont + num
print(f"Você informou {quant} números e a soma deles e {cont}.")
