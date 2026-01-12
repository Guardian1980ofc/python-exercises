from random import choice
print("-="*20)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar... ")
print("-="*20)
computador = choice([0, 1, 2, 3, 4, 5])
num = int(input("Em qual número eu pensei? "))

if num == computador:
    print(f"Parabens você acertou o numero era {num}")

else:
    print(f"Não! O Numero era {computador}")