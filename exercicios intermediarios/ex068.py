from random import choice
print("=-"*10)
print("VAMOS JOGAR IMPAR OU PAR")
print("=-"*10)

cont = 0

while True:
    computador = choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    num = int(input("Digite um valor: "))
    parouimpar = str(input("Par ou impar[P/I]: ")).upper().strip()[0]
    soma = computador + num

    if parouimpar == "P":
        if soma % 2 == 0:
            print("-"*15)
            print(f"Você jogou {num} e o computador jogou {computador} é PAR")
            print("Vitoria")
            cont +=1
            print("-"*15)

        elif soma % 2 != 0:
            print("-"*15)
            print(f"Você jogou {num} e o computador jogou {computador} é IMPAR")
            print("Derrota Brutal")
            print(f"Você ganhou {cont} vezes")
            print("-"*15)
            break

    elif parouimpar == "I":
        if soma % 2 == 0:
            print("-"*15)
            print(f"Você jogou {num} e o computador jogou {computador} é PAR")
            print("Derrota Brutal")
            print(f"Você ganhou {cont} vezes")
            print("-"*15)
            break

        elif soma % 2 != 0:
            print("-"*15)
            print(f"Você jogou {num} e o computador jogou {computador} é IMPAR")
            print("Vitoria")
            cont +=1
            print("-"*15)

