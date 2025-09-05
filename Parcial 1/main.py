# main.py
# ============================================
# Clase principal que integra los módulos:
# - Importa "ventas" para registrar las ventas
# - Importa "reportes" para calcular y mostrar resultados
# ============================================

import ventas
import reportes

class SistemaVentas:
    def ejecutar(self):
        # Paso 1: Registrar ventas (entrada de datos del usuario)
        ventas_registradas = ventas.registrar_ventas()
        
        # Paso 2: Calcular ingresos totales y por producto
        total, ingresos = reportes.calcular_ingresos(ventas_registradas)
        
        # Paso 3: Mostrar el reporte en pantalla
        reportes.mostrar_reporte(total, ingresos)


# ===========================
# Punto de inicio del programa
# ===========================
if __name__ == "__main__":
    app = SistemaVentas()
    app.ejecutar()
