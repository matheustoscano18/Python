lista = list()
pessoas = dict()
cont = quantnome = totidade = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input("Nome: "))
    quantnome += 1
    pessoas['sexo'] = str(input("Sexo: [M/F] ")).strip().upper()[0]
    while pessoas['sexo'] not in 'MF':
        print("ERRO! Por favor, digite apenas M ou F.")
        pessoas['sexo'] = str(input("Sexo: [M/F] ")).strip().upper()[0]
    pessoas['idade'] = int(input("Idade: "))
    totidade += pessoas['idade']
    lista.append(pessoas.copy())
    escolha = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    while escolha not in 'SN':
        print("ERRO! Responda apenas S ou N")
        escolha = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if escolha == 'N':
        break
    cont += 1
media = totidade / quantnome
print("-=" * 30)
print(f"A) Ao todo temos {quantnome} pessoas cadastradas.")
print(f"B) A média de idade é de {media:5.2f} anos.")
print("C) As mulheres cadastradas foram ", end='')
for p in lista:
    if p['sexo'] == 'F':
        print(f"{p['nome']}", end=' ')
print()
print("D) Lista das pessoas que estão acima da média: ")
for p in lista:
    if p['idade'] >= media:
        print('    ')
        for k, v in p.items():
            print(f"{k} = {v}; ", end='')
        print()
print("<<< ENCERRADO >>>")
