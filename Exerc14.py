from math import hypot

catOp = float(input("Comprimento do cateto oposto: "))
catAd = float(input("Comprimento do cateto adjacente: "))
hi = hypot(catAd, catOp)
print("O valor da hipotenusa é {:.2f}".format(hi))
