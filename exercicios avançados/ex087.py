matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f"Digite o valor da posição: [{i}, {j}]: "))

print("-="*30)
for i in range(0, 3):
    for j in range(0, 3):
        print(f"{matriz[i][j]:^5}", end=" ")
        if matriz[i][j] % 2 == 0:
            spar += matriz[i][j]
    print()
print("-="*30)
print(f"A soma dos valorez pares é: {spar}.")
for i in range(0, 3):
    scol += matriz[i][2]
print(f"A soma dos valorez da terceira coluna é: {scol}.")
for i in range(0, 3):
    if i == 0:
        mai = matriz[1][i]
    elif matriz[1][i]:
        mai = matriz[1][i]

print(f"O maior elemento da segunda linha é: {mai}")
