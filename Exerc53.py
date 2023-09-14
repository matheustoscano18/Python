escolha = 'S'
maior = menor = soma = cont = media = 0
while escolha == 'S':
    n = int(input("Digite um número: "))
    escolha = str(input("Quer continuar? [S/N] ")).upper().strip()
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = soma / cont
print(f"Você digitou {cont} números e a média foi {media}")
print(f"O maior valor foi {maior} e o menor foi {menor}")
