nome = str(input("Digite seu nome completo: "))
print("Analisando seu nome...")
print("Seu nome em maiúsculas é {}".format(nome.upper()))
print("Seu nome em minúsculas é {}".format(nome.lower()))
print("Seu nome tem ao todo {} letras".format(len(nome)))

divid = nome.split()
print("Seu primeiro nome é {} e ele tem {} letras".format(divid[0], len(divid[0])))
