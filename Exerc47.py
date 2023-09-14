from datetime import date
# Maior ou menor de idade
menor = 0
maior = 0
for c in range(1, 8):
    anos = int(input(f"Em que ano a {c}ª pessoa nasceu? "))
    idade = date.today().year - anos
    if idade <= 18:
        menor += 1
    else:
        maior += 1
print(f"Ao todo tivemos {maior} pessoas maiores de idade\n"
      f"E também tivemos {menor} pessoas menores de idade")
