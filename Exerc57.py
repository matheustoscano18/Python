from random import randint
num = (randint(1, 10), randint(1, 10), randint(1, 10),
       randint(1, 10), randint(1, 10))
print("Os valores sorteados foram: ", end='')
for sorteio in num:
    print(sorteio, end=' ')
print(f"\nO maior valor sorteado foi {max(num)}")
print(f"O menor valor sorteado foi {min(num)}")
