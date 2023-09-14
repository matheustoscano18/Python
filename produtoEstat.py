totvalor = valormil = menorval = cont = 0
nome_produto = ''

print("-" * 30)
print("LOJA SUPER BARATÃO")
print("-" * 30)

while True:
    nome = str(input("Nome do Produto: "))
    valor = float(input("Preço: R$"))
    cont += 1
    totvalor += valor
    if valor > 1000:
        valormil += 1
    if cont == 1 or valor < menorval:
        menorval = valor
        nome_produto = nome
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if escolha == 'N':
        break

print("------ FIM DO PROGRAMA ------")
print(f"O total da compra foi R${totvalor:.2f}")
print(f"Temos {valormil} produtos custando mais de R$1000.00")
print(f"O produto mais barato foi {nome_produto} que custa R${menorval:.2f}")
