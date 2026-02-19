times = ("Corinthians", "Palmeiras", "Santos", "Gremio", "Cruzeiro", "Flamengo", "Vasco", "Chapecoense", "Atletico", "Bota fogo",
        "Atletico-PR", "Bahia", "São paulo", "Fluminense", "Esporte recife", "EC Vitoria", "Coritiba", "Avaí", "Ponte preta", "Atletico-GO")

print("-=" *20)
print(f"Lista de times: {times}")
print("-=" *20)
print(f"Primeiros 5 times: {times[0:5]}")
print("-=" *20)
print(f"Os ultimos 4 colocados: {times[-4:]}")
print("-=" *20)
print(f"Times em ordem alfabetica: {sorted(times)}")
print("-=" *20)
print(f"O time chapecoense está na: {times.index("Chapecoense")+1} posição")