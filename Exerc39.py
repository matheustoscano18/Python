peso = float(input("Qual é seu peso? (kg) "))
altura = float(input("Qual é sua altura? (m) "))
imc = peso / altura**2
print(f"O IMC dessa pessoa é de {imc:.1f}")

if imc < 18.5:
    print("Você está ABAIXO do peso!")
elif imc < 25:
    print("Você está no peso IDEAL!")
elif imc < 30:
    print("Você está em SOBREPESO!")
elif imc < 40:
    print("Você está OBESO!")
else:
    print("Você é um OBESO MÓRBIDO!")
