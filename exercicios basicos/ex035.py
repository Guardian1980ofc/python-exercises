print("=-="*10)
print("Analise de triângulo")
print("=-="*10)

a = int(input("Digite o angulo A: "))
b = int(input("Digite o angulo B: "))
c = int(input("Digite o angulo C: "))

if b+c < a or a+c < b or a+b < c:
    print("Não é possivel criar um triângulo")

else:
    print("É possivel criar um triângulo")
