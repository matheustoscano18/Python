n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
n3 = int(input("Terceiro número: "))

if n1 < n2 and n3:
    print(f"O menor valor digitado foi {n1}")
elif n2 < n1 and n3:
    print(f"O menor valor digitado foi {n2}")
elif n3 < n1 and n2:
    print(f"O menor valor digitado foi {n3}")

if n1 > n2 and n3:
    print(f"O maior valor digitado foi {n1}")
elif n2 > n1 and n3:
    print(f"O maior valor digitado foi {n2}")
elif n3 > n1 and n2:
    print(f"O maior valor digitado foi {n3}")
