maior_homem = 0     # variavel para definir a idade do homem mais velho
nome_homem = ""
tot_mulher20 = 0    # variavel para somar a quantidade de mulheres menor que 20 anos
tot_idade = 0   # variável para somar a idade de todas as pessoas

for p in range(1, 5):
    print(f"----- {p}ª PESSOA -----")
    nome1 = str(input("Nome: "))
    idade1 = float(input("Idade: "))
    tot_idade += idade1
    sexo1 = str(input("Sexo [F/M]: ")).upper()

    if idade1 < 20 and sexo1 == 'F':
        tot_mulher20 += 1
    if idade1 == 1:
        maior_homem = idade1
    elif idade1 >= maior_homem:
        maior_homem = idade1
        nome_homem = nome1

print(f"A média de idade do grupo é de {tot_idade / 4:.1f} anos")
print(f"O homem mais velho tem {maior_homem:.0f} anos e se chama {nome_homem}")
print(f"Ao todo são {tot_mulher20} mulheres com menos de 20 anos")
