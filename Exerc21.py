# Programa que lê se tem Silva no nome
nome = str(input("Qual é seu nome completo? ")).strip()
print("Seu nome tem Silva? {}".format('SILVA' in nome.upper()))
