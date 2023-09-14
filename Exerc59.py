print("-" * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print("-" * 40)
produtos = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
for item in range(0, len(produtos)):
    if item % 2 == 0:
        print(f"{produtos[item]:.<30}", end='')
    if item % 2 == 1:
        print(f"R${produtos[item]:>7.2f}")
print("-" * 40)
