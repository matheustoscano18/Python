lista = []
while True:
    lista.append(int(input("Digite um valor: ")))
    lista.sort(reverse=True)
    escolha = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if escolha == 'N':
        break
print(f"Você digitou {len(lista)} elementos. ")
print(f"Os valores em ordem decrescente são {lista}")
if 5 not in lista:
    print("O valor 5 não faz parte da lista!")
else:
    print("O valor 5 faz parte da lista!")
