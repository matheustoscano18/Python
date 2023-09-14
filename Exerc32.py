valor = float(input("Valor da casa: R$"))
salario = float(input("Salário do comprador: R$"))
ano_finan = int(input("Quantos anos de financiamento? "))
prestacao = valor / (ano_finan * 12)
print(f"Para pagar uma casa de R${valor:.2f} em {ano_finan} anos a prestação será de R${prestacao:.2f}")

if prestacao > (30 / 100 * salario):
    print("Empréstimo NEGADO!")
else:
    print("Empréstimo PODE SER CONCEDIDO!")
