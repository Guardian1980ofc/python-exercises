num = int(input("Digite um numero: "))
contador = 3
t1 = 0
t2 = 1

print(f"{t1}, {t2}", end=" ")
while contador <= num:
    t3 = t1 + t2
    print(f", {t3}", end=" ")
    t1 = t2
    t2 = t3
    contador+=1

print(", Fim")