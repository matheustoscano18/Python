escolha = ''
num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
       'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove',
       'vinte')
while True:
    dig = int(input("Digite um número entre 0 e 20: "))
    if 0 <= dig <= 20:
        print(f"Você digitou o número {num[dig]}")
    else:
        print("Tente novamente. ", end='')
    escolha = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if escolha == 'N':
        break
