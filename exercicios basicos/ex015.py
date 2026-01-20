dias = int(input("Quantos dias o carro ficou alugado: "))
km = float(input("Quantos km rodados: "))
pago = dias * 60 + km * 0.15

print(f"Total a pagar é de R${pago:.2f}")