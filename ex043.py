peso = float(input("Qual o seu peso? (Kg)"))
altura = float(input("Qual sua altura? (m)"))

imc = peso / (altura**2)

print(f"O IMC dessa pessoa é de {imc}")

if imc <= 18.5:
    print("Você está em ABAIXO DO PESO, cuidado")
elif 18.5 < imc <= 25.0:
    print("Você esta em PESO IDEAL")
elif 25.0 < imc <= 30.0:
    print("Você está em SOBREPESO")
elif 30.0 < imc <= 40.0:
    print("Você está em Obesidade, seu porpeta")
elif imc > 40.0:
    print("Você está em OBESIDADE MORBÍDA, CUIDADO!!!!")
