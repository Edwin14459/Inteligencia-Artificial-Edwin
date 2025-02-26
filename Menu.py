import subprocess

ejercicios = [
    ("Declaración de variables", "Ejercicio01.py"),
    ("Datos de estudiante", "Ejercicio2.py"),
    ("Resta, multiplicación y nombre", "Ejercicio3.py"),
    ("Entrada de datos", "Ejercicio4.py"),
    ("Entrada de datos de suma", "Ejercicio5.py"),
    ("Resta y multiplicación", "Ejercicio6.py"),
    ("Calcular área de un círculo", "Ejercicio7.py"),
    ("Número par o impar", "Ejercicio8.py"),
    ("Mayor que 10", "Ejercicio10.py"),
    ("Número positivo o negativo", "Ejercicio11.py"),
    ("Adivinar un número", "Ejercicio12.py"),
    ("Uso de librería Datetime", "Ejercicio13.py"),
    ("Mostrar calificación por letra", "Ejercicio14.py"),
    ("Realizar el 10% de descuento", "Ejercicio15.py"),
    ("Realizar el 10% de descuento 1ra mejora", "Ejercicio151ra.py"),
    ("Realizar el 10% de descuento 2da mejora", "Ejercicio152da.py"),
    ("Agente Cognoscitivo", "Ejercicio16.py"),
    ("Sistema Multiagente", "Ejercicio17.py"),
    ("El papel de la heurística", "Ejercicio18.py"),
    ("Algoritmos de Exploración alternativa DFS", "Ejercicio19.py"),
    ("Algoritmo A Camino más corto", "Ejercicio20.py"),
    ("Algoritmo A", "Ejercicio21.py"),
    ("Algoritmo de búsqueda local", "Ejercicio22.py")
]

while True:
    print("\n-----Bienvenido al Menú de Ejercicios en Python-----")
    for i, (nombre, _) in enumerate(ejercicios, 1):
        print(f"{i}. {nombre}")
    print(f"{len(ejercicios) + 1}. Salir del Menú")

    opcion = input("Selecciona una opción del 1 al 24: ")
    print()

    if opcion.isdigit():
        opcion = int(opcion)
        if 1 <= opcion <= len(ejercicios):
            subprocess.run(["python", ejercicios[opcion - 1][1]])
        elif opcion == len(ejercicios) + 1:
            print("¡Hasta luego!")
            break
    else:
        print("Opción Invalida. Porfavor ingrese un número válido.")
