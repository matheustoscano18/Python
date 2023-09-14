def leiadinheiro(n):
    ok = False
    while not ok:
        entrada = str(input(n)).replace(',', '.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f'\033[0;31mERRO! "{entrada}" é um preço inválido!\033[m')
        else:
            ok = True
            return float(entrada)
