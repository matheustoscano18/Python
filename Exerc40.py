print("===" * 4, end='')
print(" LOJAS TOSCANO ", end='')
print("===" * 4)
preco = float(input("Preço das compras: "))
print("FORMAS DE PAGAMENTO\n"
      "[ 1 ] à vista dinhero/cheque\n"
      "[ 2 ] à vista cartão\n"
      "[ 3 ] 2x no cartão\n"
      "[ 4 ] 3x ou mais no cartão")
opcao = int(input("Qual é a opção? "))

if opcao == 1:
    print(f"Sua compra de R${preco:.2f} vai custar R${preco - (10 / 100 * preco):.2f} no final.")
elif opcao == 2:
    print(f"Sua compra de R${preco:.2f} vai custar R${preco - (5 / 100 * preco):.2f} no cartão à vista.")
elif opcao == 3:
    print(f"Sua compra será parcelada em 2x de {preco / 2:.2f} SEM JUROS\n"
          f"Sua compra custará R${preco:.2f} no final.")
elif opcao == 4:
    parcela = int(input("Quantas parcelas? "))
    juros = 20 / 100 * preco
    print(f"Sua compra será parcelada em {parcela}x de R${(preco + juros) / parcela:.2f} COM JUROS\n"
          f"Sua compra de R${preco:.2f} vai custar R${preco + juros:.2f} ")
else:
    print("COMANDO INVÁLIDO!")
