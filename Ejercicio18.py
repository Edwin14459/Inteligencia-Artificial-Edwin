# Heurística simple para encontrar el número más cercano al objetivo
def heuristica(a, b):
    return abs(a - b)

# Resolver un problema simple
objetivo = 50
valores = [20, 35, 55, 60, 70]

# Encontrar el valor más cercano al objetivo usando heurística
mejor_valor = min(valores, key=lambda x: heuristica(x, objetivo))
print(f"El valor más cercano al objetivo {objetivo} es: {mejor_valor}")