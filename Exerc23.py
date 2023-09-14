nome = str(input("Digite seu nome completo: "))
nome1 = nome.split()

print("Muito prazer em te conhecer!")
print("Seu primeiro nome é {}".format(nome1[0]))
print("Seu último nome é {}".format(nome1[len(nome1)-1]))
