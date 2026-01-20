distancia = int(input("Digite a distancia ds visgem em Km: "))

if distancia <= 200:
    custo = distancia * 0.50
else:
    custo = distancia * 0.45

print(f"A sua viajem de {distancia} ira custar R${custo:.2f}")
