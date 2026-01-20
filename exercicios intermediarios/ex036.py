valorCasa = float(input("Digite o valor da casa que deseja comprar: "))
salario = float(input("Digite o seu salario: "))
periodoPagamento = int(input("Em quantos anos você ira pagar a casa? "))

parcelasMensais = valorCasa / (periodoPagamento * 12)

porcentagemMax = salario * 0.30

print(f"Para pagar uma casa de R${valorCasa:.2f} em {periodoPagamento} anos a prestação mensal será de R${parcelasMensais:.2f}")

if parcelasMensais <= porcentagemMax:
    print("Emprestimo aprovado")

else:
    print("Emprestimo recusado")