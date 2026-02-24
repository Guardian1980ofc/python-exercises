numeros = []
num_pares = []
num_impares = []

while True:
    numeros.append(int(input("Digite um numero: ")))

    resposta = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]
    if resposta == "N":
        break

for num in numeros:
    if num % 2 == 0:
        num_pares.append(num)
    else:
        num_impares.append(num)

print(f"Números digitados: {numeros}")
print(f"Pares: {num_pares}")
print(f"Ímpares: {num_impares}")
print("Fim do programa...")
