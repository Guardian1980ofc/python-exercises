numeros = []
while True:
    n = int(input("Digite um numero: "))
    if n not in numeros:
        numeros.append(n)
        print("Valor adicionado com sucesso>")

    else:
        print("Valor duplicado! Não vou adicionar")

    pergunta = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if pergunta == "N":
        break
    
print("=-"*30)
numeros.sort()
print(f"Você digitou {len(numeros)} números")
print(f"Os valores foram: {numeros}")
