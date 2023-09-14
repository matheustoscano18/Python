from datetime import date
atual = date.today().year
ano = int(input("Ano de nascimento: "))
idade = atual - ano
print(f"Quem nasceu em {ano} tem {idade} em 2023")

if idade < 18:
    print(f"Ainda faltam {18 - idade} para o alistamento!\n"
          f"Seu alistamento será em {18 + ano}. ")
elif idade > 18:
    print(f"Você já deveria ter se alistado há {idade - 18} anos.\n"
          f"Seu alistamento foi em {18 + ano}")
else:
    print("Você deve se alistar IMEDIATAMENTE! ")
