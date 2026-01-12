largura = float(input("Largura da parede:"))
Altura = float(input("Altura da parede:"))

area = largura * Altura
litros = area / 2

print(f"Com uma parede com a área de {area}m vai precisar de {litros:.1f} litros de tinta para pintala por completo")