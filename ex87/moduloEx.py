import moeda
from time import sleep

num = float(input("Digite o preço: R$"))
print(f"A metade de {moeda.moeda(num)} é {moeda.metade(num, True)}")
print(f"O dobro de {moeda.moeda(num)} é {moeda.dobro(num, True)}")
print(f"Aumentando 10%, temos {moeda.aumentar(num, 10, True)}")
print(f"Reduzindo 20%, temos {moeda.diminuir(num, 20, True)}")
# sleep(5)
# help(moeda)