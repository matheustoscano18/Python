n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1 + n2) / 2
print(f"Tirando {n1:.2f} e {n2:.2f}, a média do aluno é {media:.2f}")
if media >= 7:
    print("O aluno está APROVADO!")
elif 7 > media >= 5:
    print("O aluno está de RECUPERAÇÃO.")
else:
    print("O aluno está REPROVADO!")
