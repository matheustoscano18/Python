num = int(input("Digite um número inteiro: "))
print("Escolha uma das bases para conversão:\n"
      "[ 1 ] Converter para BINÁRIO\n"
      "[ 2 ] Converter para OCTAL\n"
      "[ 3 ] Converter para HEXADECIMAL\n")
valor = int(input("Sua opção: "))
if valor == 1:
    print(f"{num} convertido para BINÁRIO é igual a {bin(num)[2:]}")
elif valor == 2:
    print(f"{num} convertido para OCTAL é igual a {oct(num)[2:]}")
elif valor == 3:
    print(f"{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}")
else:
    print("COMANDO INVÁLIDO! Tente novamente!")
