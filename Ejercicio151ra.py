nombre = input("Ingrese su nombre: ")
producto = input("Ingrese el nombre del producto: ")
total_compra = float(input("Ingrese el total de tu compra: "))
total_final = total_compra
if total_compra > 100:
    descuento = total_compra * 0.10
    total_final = total_compra - descuento
    print(f"Felicidades {nombre}! Tienes un descuento del 10% de tu producto: {producto}")
    print(f"El total a pagar es: {total_final}")  