n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
opção = 0
while opção != 5:
    print('''
    [ 1 ] SOMAR
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos numeros
    [ 5 ] sair do programa
          ''')
    
    opção = int(input("Qual é sua opção: "))

    if opção == 1:
        print(f"A soma entre {n1} e {n2} é {n1 + n2}")

    elif opção == 2:
        print(f"O produto de {n1} e {n2} é {n1 * n2}")

    elif opção == 3:
        if n1 > n2:
            print(f"{n1} é o maior numero")

    elif opção == 4:
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor"))

    elif opção == 5:
        print("Finalizando...")

    else:
        print("Opção invalida tente novamente")

print("fim do programa...")