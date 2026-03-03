pessoas = []
dados = []
maior_P = menor_P = 0

while True:
    dados.append(str(input("Nome: ")))
    dados.append(float(input("Peso: ")))

    if len(pessoas) == 0:
        maior_P = menor_P = dados[1]
    else:
        if dados[1] > maior_P:
            maior_P = dados[1]

        if dados[1] < menor_P:
            menor_P = dados[1]

    pessoas.append(dados[:])
    dados.clear()

    resp = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]
    if resp == "N":
        break

print(pessoas)
print(f"Você cadastrou um total de {len(pessoas)} pessoas")
print(f"O maior peso foi de {maior_P}Kg, Peso de ", end=" ")
for p in pessoas:
    if p[1] == maior_P:
        print(f"{p[0]}", end=" ")
print()
print(f"O menor peso foi de {menor_P}Kg, peso de ", end=" ")
for p in pessoas:
    if p[1] == menor_P:
        print(f"{p[0]}", end=" ")
print()
print("Programa encerrado...")
