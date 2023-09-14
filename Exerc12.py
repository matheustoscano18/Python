alug_dia = int(input("Quantos dias o carro foi alugado? "))

km_carro = float(input("Quantos km rodados? "))

total = (alug_dia * 60) + (km_carro * 0.15)

print("O total a pagar é de R${:.2f}".format(total))
