from random import choice
computador = choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print("tente adivinhar em qual numero eu estou pensando.")
print("É um numero de 0 a 10")

num = int(input("qual o seu palpite? "))
tentativas = 0

if num == computador:
    print("Parabens voce acertou de primeira")

elif num != computador:
    while num != computador:
        if num > computador:
            num = int(input("menos, :"))
        elif num < computador:
            num = int(input("mais, : "))
        tentativas +=1
print(f"Isso! Você acertou o numero {computador}, com {tentativas} tentativas")
