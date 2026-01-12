num = int(input("Digite um numero inteiro: "))
print('''Qual opção você escolhe?
[1] transformar em binario
[2] em octal
[3] em hexadecimal''')
opção = int(input("Sua opção: "))
if opção == 1:
    print(f"{num} convertido em binario é igual a {bin(num)[2:]}")
elif opção == 2:
    print(f"{num} convertido em OCTAL é igual a {oct(num)[2:]}")
elif opção == 3:
    print(f"{num} convertido em Hexadecimal é igual a {hex(num)[2:]}")
else:
    print("Opção invalida tente novamente...")

print("Progama encerrado")
