sexo = (str(input("Informe seu sexo: [F/M] "))).upper()
while sexo != 'F' and sexo != 'M':
    sexo = str(input("Sexo invalido! digite novamente ")).upper()

print(f"Sexo {sexo} validado")
