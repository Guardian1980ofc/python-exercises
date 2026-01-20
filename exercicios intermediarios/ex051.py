print("=="*10)
print("=="*10)

primeiro = int(input("Primeiro termo: "))
razão = int(input("Razão: "))
decimo = primeiro + (10 - 1) * razão
for c in range(primeiro, decimo, razão):
    print(f"{c}", end=" ")
print("Acabou")
