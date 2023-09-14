jogador = dict()
lista = list()
cont = 0
while True:
    jogador['nome'] = str(input("Nome do jogador: "))
    partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    for c in range(0, partidas):
        lista.append(int(input(f"Quantas gols na partida {c+1}? ")))
    jogador['gols'] = lista[:]
    jogador['total'] = sum(lista)
    resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if resp == 'N':
        break
print("-=" * 30)
print("cod nome \t\t gols\t\t total")
