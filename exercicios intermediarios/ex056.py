soma_idade = 0
homem_velho = ""
idade_homem_velho = 0
mulheres20 = 0

for p in range(1, 5):
    nome = str(input(f"Qual o nome da {p} pessoa: "))
    idade = int(input("Qual a idade dessa pessoa: "))
    sexo = str(input("Qual o sexo dessa pessoa(M/F): ")).upper()
    
    soma_idade += idade

    if sexo == "M":
        if idade > idade_homem_velho:
            idade_homem_velho = idade
            homem_velho = nome

    if sexo == "F":
        if idade < 20:
            mulheres20 += 1

media = soma_idade / 4

print(f"A media das idades foi {media}, \nO homem mais velho foi {homem_velho} com {idade_homem_velho} anos \n e {mulheres20} mulheres tinham menos de vinte anos")
