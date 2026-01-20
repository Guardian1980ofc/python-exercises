valor_org = float(input("Qual o valor do produto? "))

desconto = valor_org * 0.05
valor_novo = valor_org - desconto

print(f"O produto que custa R${valor_org} com um desconto de 5% passara a custar R${valor_novo:.2f}")
