import datetime

nombre = input("Ingrese su nombre: ")

fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Nombre del cliente: {nombre} y la Fecha y hora actual: {fecha} ")