n1 = cont = total = 0
n1 = int(input("Digite um número [999 para parar]: "))
while n1 != 999:
    total += n1
    cont += 1
    n1 = int(input("Digite um número [999 para parar]: "))
print(f"Você digitou {cont} números e a soma entre eles foi {total}.")
