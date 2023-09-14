dist = float(input("Qual a distância da sua viagem? "))
viagemC = 0.50 * dist
viagemL = 0.45 * dist
print(f"Você está prestes a fazer uma viagem de {dist:.1f}km.")
if dist <= 200:
    print("E o preço da sua passagem será de R${:.2f}".format(viagemC))
else:
    print("E o preço da sua passagem será de R${:.2f}".format(viagemL))
