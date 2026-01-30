contador = 0
soma = num = 0
num = int(input("Digite um numero[999 para sair]: "))

while num != 999:
    soma+=num
    contador+=1
    num = int(input("Digite um numero[999 para sair]: "))


print(f"Você digitou {contador} numeros e a soma deles deu {soma}")
print("Programa finalizado...")