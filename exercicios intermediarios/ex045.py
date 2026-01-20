from random import randint
itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0, 2)
print('''[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input("Sua jogada: "))
print("-=" * 10)
print(f"Computador escolheu {computador}")
print(f"Jogador escolheu {jogador}")
print("-=" * 10)
if computador == 0:
    if jogador == 0:
        print("Empatou")
    elif jogador == 1:
        print("O jogador ganhou")
    elif jogador == 2:
        print("O computador ganhou")
    else:
        print("Jogada invalida")

elif computador == 1:
    if jogador == 1:
            print("Empatou")
    elif jogador == 2:
        print("O jogador ganhou")
    elif jogador == 0:
        print("O computador ganhou")
    else:
        print("Jogada invalida")

elif computador == 2:
    if jogador == 2:
            print("Empatou")
    elif jogador == 0:
        print("O jogador ganhou")
    elif jogador == 1:
        print("O computador ganhou")
    else:
        print("Jogada invalida")
