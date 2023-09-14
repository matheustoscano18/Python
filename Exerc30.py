sal = float(input("Qual é o salário do funcionário? R$"))
sal_menor = sal + (15 / 100 * sal)
sal_maior = sal + (10 / 100 * sal)

if sal <= 1250:
    print(f"Quem ganhava R${sal:.2f} passa a ganhar R${sal_menor:.2f} agora.")
else:
    print(f"Quem ganhava R${sal} passa a ganhar R${sal_maior} agora.")
