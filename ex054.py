from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for pess in range(1, 8):
    nasc = int(input(f"Em que ano a {pess} pessoa nasceu? "))
    idade = atual - nasc
    if idade >= 21:
        totalmaior+=1
    else:
        totalmenor+=1
print(f"Ao todo tivemos {totalmaior} pessoas maior de idade")
print(f"E tambem tivemos {totalmenor} pessoas menor de idade")