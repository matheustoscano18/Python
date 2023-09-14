import math

angulo = float(input("Digite o ângulo que você deseja: "))
angRad = math.radians(angulo)
print("O ângulo de {} tem o SENO de {:.2f}".format(angulo, math.sin(angRad)))
print("o ângulo de {} tem o COSSENO de {:.2f}".format(angulo, math.cos(angRad)))
print("O ãngulo de {} tem a TANGENTE de {:.2f}".format(angulo, math.tan(angRad)))
