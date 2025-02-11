import random
import datetime

tienda = "Tienda López"
nombre = input("Nombre del cliente: ")
producto = input("Producto del cliente: ")
total = float(input("Total de la compra: "))

folio = random.randint(1, 100)  
fecha = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")

descuento = 0
total_final = total
if total > 100:
    descuento = total * 0.10
    total_final = total - descuento

print("\n============ TICKET DE COMPRA ============")
print(f"Tienda: {tienda}")
print(f"Folio: {folio}")
print(f"Fecha: {fecha}")
print("-----------------------------------------")
print(f"Cliente: {nombre}")
print(f"Producto: {producto}")
print(f"Total: ${total}")
print(f"Descuento: ${descuento}")
print(f"Total a pagar: ${total_final}")
print("-----------------------------------------")
print("¡Gracias por tu compra!. ¡Vuelva pronto!")
print("=========================================")
