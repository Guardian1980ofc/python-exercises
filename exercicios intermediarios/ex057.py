sexo = str(input("Digite o seu sexo(M/F): ")).upper()
while sexo not in "MmFf":
    sexo = str(input("Dados invalidos. Por favor infrme seu sexo: "))
print(f"Sexo {sexo} registrado com sucesso")