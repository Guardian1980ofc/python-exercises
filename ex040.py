nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1+nota2)/2

print(f"Tirando {nota1} e {nota2}, a media do aluno é {media:.1f}")

if media >= 7.0:
    print("O aluno foi aprovado")
elif media < 7.0 and media > 5.0:
    print("O aluno foi pra recuperação")
else:
    print("O aluno foi reprovado")
