car_veloc = float(input("Qual a velocidade atual do seu carro? "))
multa = ((car_veloc - 80) * 7)
if car_veloc > 80:
    print("MULTADO! Você excedeu o limite permitido da via que é de 80km/h\n"
          "Você deve pagar uma multa de R${:.2f}".format(multa))
print("Tenha um bom dia! Dirija com segurança!")
