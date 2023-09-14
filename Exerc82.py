def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    print(f"Com {idade} anos: ", end='')
    if idade < 16:
        print("NÃO VOTA")
    elif 16 <= idade < 18 or idade > 70:
        print("VOTO OPCIONAL")
    else:
        print("VOTO OBRIGATÓRIO")


print("-" * 30)
nasc = int(input("Em que ano você nasceu? "))
voto(nasc)
