from time import sleep

# CONTAGEM REGRESSIVA
n = int(input("Digite um número: "))
for n in range(n, 0, -1):
    print(n)
    sleep(1)
print("BOOM! POW! BOOOOM!")
