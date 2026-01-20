print(f"{" LOJAS GUANABARAS ":=^40}")
preço = float(input("Preço das compras: R$"))
print('''FORMA DE PAGAMENTO
[ 1 ] à vista no dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

opção = int(input("Qual a opção? "))
if opção == 1:
    total = preço - (preço * 0.10)
elif opção == 2:
    total = preço - (preço * 0.05)
    print(f"Sua compra de R${preço:.2f} vai custar R${total:.2f} no final.")
elif opção == 3:
    total = preço
    parcela == total / 2
    print(f"Sua compra sera parcelada e,  2x de {parcela:.2f}")
elif opção == 4:
    total == preço + (preço * 0.2)
    totalParcela = int(input("Quantas parcelas? "))
    parcela = total / totalParcela
    print(f"Sua compra sera parcelada e,  {totalParcela}x de {parcela:.2f}")
else:
    total = 0
    print("OPÇÃO INVALIDA. Tente novamente")
print(f"Sua compra de R${preço:.2f} vai custar R${total:.2f} no final.")
