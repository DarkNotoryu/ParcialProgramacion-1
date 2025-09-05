# reportes.py
# ============================================
# Este módulo procesa los datos de ventas:
# - Calcula el ingreso total
# - Calcula el ingreso por producto
# - Muestra un reporte ordenado en pantalla
# ============================================

def calcular_ingresos(ventas):
    ingresos_totales = 0
    ingresos_por_producto = {}

    # Recorremos las ventas para calcular ingresos
    for v in ventas:
        ingreso = v["precio"] * v["cantidad"]  # ingreso = precio * cantidad
        ingresos_totales += ingreso            # Se suma al total

        # Acumulamos ingresos por producto
        if v["producto"] in ingresos_por_producto:
            ingresos_por_producto[v["producto"]] += ingreso
        else:
            ingresos_por_producto[v["producto"]] = ingreso

    return ingresos_totales, ingresos_por_producto


def mostrar_reporte(ingresos_totales, ingresos_por_producto):
    print("\n=== REPORTE DE VENTAS ===")
    print(f"Ingreso total: ${ingresos_totales:.2f}")
    
    print("\nIngresos por producto (ordenado de mayor a menor):")
    # Ordenamos los productos por ingreso en orden descendente
    for prod, ingreso in sorted(ingresos_por_producto.items(), key=lambda x: x[1], reverse=True):
        print(f"{prod}: ${ingreso:.2f}")
