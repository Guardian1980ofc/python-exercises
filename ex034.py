salario = int(input("Digite o seu salario:"))

if salario < 1250:
    ajuste = salario * 0.15 + salario
    
else:
    ajuste = salario * 0.10 + salario

print(f"O seu salario era {salario} e com o ajuste ficou {ajuste}")
