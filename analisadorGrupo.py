tot18 = tothomem = totmulher20 = 0
while True:
    print("-" * 20)
    print("CADASTRE UMA PESSOA")
    print("-" * 20)
    idade = int(input("Idade: "))
    sexo = str(input("Sexo: [M/F] ")).strip().upper()[0]
    print("-" * 20)
    escolha = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        tothomem += 1
    if sexo == 'F' and idade < 20:
        totmulher20 += 1
    if escolha == 'N':
        break
print(f"Total de pessoas com mais de 18 anos: {tot18}")
print(f"Ao todo temos {tothomem} homens cadastrados.")
print(f"E temos {totmulher20} mulheres com menos de 20 anos.")
