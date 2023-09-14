seg1 = int(input("Primeiro segmento: "))
seg2 = int(input("Segundo segmento: "))
seg3 = int(input("Terceiro segmento: "))

if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print("Os segmentos acima PODEM FORMAR um triângulo ", end='')
    if seg1 == seg2 == seg3:
        print("EQUILÁTERO")
    elif seg1 != seg2 != seg3 != seg1:
        print("ESCALENO")
    else:
        print("ISÓSCELES")
else:
    print("Os segmentos acima NÃO PODEM FORMAR um triângulo.")
