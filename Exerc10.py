salario = float(input("Qual é o salário do funcionário? R$"))

aumento = int(input("Quantos % de aumento? "))

valor = salario+(salario * aumento/100)

print(f"Um funcionário que ganhava R${salario}, com {aumento}% de aumento, passa a receber R${valor:.2f}")
