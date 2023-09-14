def area(larg, comp):
    mult = larg * comp
    print(f"A área de um terreno {larg:.1f}x{comp:.1f} é de {mult}m²")


#  Programa Principal
print(" Controle de Terrenos")
print("-" * 30)
larg = float(input("LARGURA(m): "))
comp = float(input("COMPRIMENTO(m): "))
area(larg, comp)
