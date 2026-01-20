import math
angulo = float(input("Digite um angulo: "))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print(f"O seno desse angulo é {seno:.2f}, a tangente é {tan:.2f} e o cosseno é {cos:.2f}")