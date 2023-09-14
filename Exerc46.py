nome = str(input("Digite uma frase: ")).strip().upper()
palavras = nome.split()
junto = ''.join(palavras)

inv = junto[::-1]

# Inverter nome com loop for
'''inv = ''
for letra in range(len(junto) -1, -1, -1): 
    inv += junto[letra]'''


print(f"O inverso de {junto} é {inv}")
if inv == junto:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo")
