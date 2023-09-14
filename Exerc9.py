preco = float(input("Qual o preço do produto? R$"))

desc = int(input("Quantos % de desconto? "))

valor = preco - (preco * desc/100)

print(f"O produto que custava R${preco:.2f}, na promoção com desconto de {desc}% vai custar R${valor:.2f}")
