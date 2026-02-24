listanum = []
maiornum = menornum = 0
for n in range(0, 5):
    listanum.append(int(input(f"Digite um valor para a posição {n}: ")))
    if n == 0:
        maiornum = menornum = listanum[n]

    else:
        if listanum[n] > maiornum:
            maiornum = listanum[n]

        if listanum[n] < menornum:
            menornum = listanum[n]

print("-="*30)
print(f"Você digitou os valores {listanum}")
print(f"O maior valor digitado foi {maiornum} nas posições", end=" ")

for i, v in enumerate(listanum):
    if v == maiornum:
        print(f"{i}...", end=" ")
print()

print(f"O menor valor digitado foi {menornum} nas posições", end=" ")
for i, v in enumerate(listanum):
    if v == menornum:
        print(f"{i}...", end=" ")
print()
