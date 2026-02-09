tot18 = 0
totman = 0
totwoman = 0
while True:
    idade = int(input("Idade: "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Sexo[M/F]: "))
    resposta = " "
    if idade >= 18:
        tot18+=1
    if sexo == "M":
        totman+=1
    if sexo == "F" and idade < 20:
        totwoman+=1
    while resposta not in "SN":
        resposta = str(input("Quer continuar?[S/N] ")).upper().strip()[0]
    if resposta == "N":
        break

print(f"Total de pessoas com mais de 18 anos: {tot18}")
print(f"Ao todo temos {totman} homens cadastrados")
print(f"Temos {totwoman} mulheres com menos de 20 anos")