velocidade = int(input("Qual a velocidade atual do veiculo: "))

if velocidade <= 80:
    print("Muito bem! Você está na velocidade adequada, boa viajem.")

else:
    multa = (velocidade - 80)* 7
    print(f"Você ultrapassou o limite de velocidade que é 80 km/h. A multa sera R$7,00 por Km assima do  limite, sera: R${multa:.2f}")