# Simulación de un agente cognoscitivo tomando decisiones basadas en criterios predefinidos
opciones = ["ir al cine", "estudiar", "hacer ejercicio"]

# Función para tomar una decisión basada en prioridades
def tomar_decision(prioridades):
    for opcion in opciones:
        if opcion in prioridades:
            return f"El agente decide: {opcion}"
    return "El agente no decide nada."

# Ejemplo de uso con diferentes prioridades
prioridades = ["hacer ejercicio", "estudiar"]
print(tomar_decision(prioridades))