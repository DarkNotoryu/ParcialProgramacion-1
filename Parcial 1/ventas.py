# ventas.py
# ============================================
# Este módulo se encarga de registrar las ventas.
# Pide al usuario datos de productos (nombre, precio y cantidad)
# y devuelve la información para que pueda procesarse después.
# ============================================

def registrar_ventas():
    ventas = []  # Lista donde guardaremos cada producto como un diccionario
    n = int(input("¿Cuántos productos deseas registrar hoy? "))
    
    for i in range(n):
        # Se piden los datos de cada producto
        nombre = input(f"Producto {i+1}: ")
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad vendida: "))
        
        # Guardamos la información en un diccionario
        ventas.append({"producto": nombre, "precio": precio, "cantidad": cantidad})
    
    return ventas  # Regresamos la lista de ventas
