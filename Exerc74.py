jogador = dict()
lista = list()
time = list()
cont = 0
while True:
    jogador.clear()
    jogador['nome'] = str(input("Nome do jogador: "))
    partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    lista.clear()
    for c in range(0, partidas):
        lista.append(int(input(f"Quantas gols na partida {c+1}? ")))
    jogador['gols'] = lista[:]
    jogador['total'] = sum(lista)
    time.append(jogador.copy())
    while True:
        resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
        if resp in 'SN':
            break
        print("ERRO! Responda apenas S ou N.")
    if resp == 'N':
        break
print("-" * 40)
print("cod ", end='')
for i in jogador.keys():
    print(f"{i:<15}", end='')
print()
print("-" * 40)
for k, v in enumerate(time):
    print(f"{k:>3} ", end='')
    for d in v.values():
        print(f"{str(d):<15}", end='')
    print()
print("-" * 40)
while True:
    escolha = int(input("Mostrar dados de qual jogador? (999 para parar)"))
    if escolha == 999:
        break
    if escolha >= len(time):
        print(f"Erro! não existe jogador com código {escolha}!")
    else:
        print(f" -- LEVANTAMENTO DO JOGADOR {time[escolha]['nome']}:")
        for i, g in enumerate(time[escolha]['gols']):
            print(f"    No jogo {i+1} fez {g} gols.")
    print("-" * 40)
print("VOLTE SEMPRE!")
