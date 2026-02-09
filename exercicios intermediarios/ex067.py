while True:
    print(" ")
    num = int(input("Quer ver a tabuáda de qual numero? "))

    for i in range(0, 11):
        print(f"{num} x {i} = {num * i}")

    if num < 0:
        break
