import math

#Pedir el radio del circulo
radio = float(input("Introduce el radio del circulo en metros:\n"))

#Calcular en area de circulo (A = pi r ala 2)
area = math.pi * (radio ** 2)

#Mostrar el Resultado
print(f"\nEl area del circulo con radio: {radio} metros es: {area:.2f} metros cuadrados.")