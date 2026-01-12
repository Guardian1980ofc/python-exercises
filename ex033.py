num_1 = int(input("Digite um numero: "))
num_2 = int(input("Digite outro numero: "))
num_3 = int(input("Digite mais um numero: "))

if num_1 < num_2 and num_1 < num_3:
    print(f"O numero {num_1} é o menor numero")

elif num_2 < num_1 and num_2 < num_3:
    print(f"O numero {num_2} é o menor numero")

else:
    print(f"O numero {num_3} é o menor numero")

if num_1 > num_2 and num_1 > num_3:
    print(f"O numero {num_1} é o maior numero")

elif num_2 > num_1 and num_2 > num_3:
    print(f"O numero {num_2} é o maior numero")

else:
    print(f"O numero {num_3} é o maior numero")
