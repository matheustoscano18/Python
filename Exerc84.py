def ficha(nome, gols):
    print("-" * 30)
    if len(nome) == 0:
        nome = '<desconhecido>'
    print(f"O jogador {nome} fez {gols} gol(s) no campeonato.")


# Programa principal
n = str(input("Nome do jogador: "))
g = str(input("Número de gols: "))
if g.isnumeric():
    g = int(g)
else:
    g = 0
ficha(n, g)
