from random import shuffle

n1 = str(input("Digite o nome o primeiro aluno: "))
n2 = str(input("Digite o nome o segundo aluno: "))
n3 = str(input("Digite o nome o terceiro aluno: "))
n4 = str(input("Digite o nome o quarto aluno: "))

lista = [n1, n2, n3, n4]
shuffle(lista)

print(f"A ordem de apresentação é {lista}")
