from time import sleep

num1 = int(input("Primeiro valor: "))
num2 = int(input("Segundo valor: "))
opcao = 0
while True:
    print("[ 1 ] SOMAR\n"
          "[ 2 ] MULTIPLICAR\n"
          "[ 3 ] MAIOR\n"
          "[ 4 ] NOVOS NÚMEROS\n"
          "[ 5 ] SAIR DO PROGRAMA\n")
    opcao = int(input(">>>>> Qual é a sua opção? "))
    if opcao == 1:
        soma = num1 + num2
        print(f"A soma entre {num1} + {num2} é {soma}")
    elif opcao == 2:
        mult = num1 * num2
        print(f"O resultado de {num1} x {num2} é {mult}")
    elif opcao == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print(f"Entre {num1} e {num2} o maior valor é {maior}")
    elif opcao == 4:
        print("Informe os números novamente: ")
        num1 = int(input("Primeiro valor: "))
        num2 = int(input("Segundo valor: "))
    elif opcao == 5:
        print("Encerrando menu...")
        sleep(2)
        print("Fim do Programa!")
        break
    else:
        print("COMANDO INVÁLIDO!")
    print("=-=" * 10)
