def leiaint(msg):
    while True:
        try:
            numint = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: Por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mUsuário não digitou um número!\033[m')
        else:
            return numint


def leiafloat(msg):
    while True:
        try:
            numfloat = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: Por favor, digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mUsuário não digitou um número!\033[m')
        else:
            return numfloat


# Programa principal
num = leiaint('Digite um inteiro: ')
numf = leiafloat('Digite um Real: ')
print(f"O valor inteiro digitado foi {num} e o real foi {numf}")
