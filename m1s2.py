# Importamos las funciones desde utils.py
from utils import agregar_producto
from utils import mostrar_inventario
from utils import calcular_estadisticas
import os
inventario1 = []

# Lista principal del inventario
# Función para limpiar la consola (Windows / Linux / Mac)
def clear():
    os.system("cls" if os.name == "nt" else "clear")
# Bucle principal del programa 
while True:
    # Menú de opciones
    opcion = int(input("""Seleccione una de las siguientes opciones:
    1. Agregar producto
    2. Mostrar inventario
    3. Calcular estadísticas
    4. Salir

    Ingrese su opción: """))
    # Opción 1: Agregar producto
    if opcion == 1:
        clear()
        # Se guarda la lista actualizada que retorna la función
        inventario1 = agregar_producto()
    # Opción 2: Mostrar inventario
    elif opcion == 2:
        clear()
        if not inventario1:  # validar si está vacío
            print("El inventario está vacío")
        else:
    # Mostramos los productos    
            mostrar_inventario(inventario1)  # mostrar la lista real
    elif opcion == 3:
        clear()
        if not inventario1:  # validar si está vacío
            print("Estadisticas no disponibles. El inventario está vacío")
        else:
    # Calculamos totales
            calcular_estadisticas(inventario1) 
    # Opción 4: Salir del programa
    elif opcion == 4:
        print("Adios")
        break
        
    else:
        print(" Opción inválida, intenta nuevamente")
# -----------------------------------------------------------------
# Notas sobre lo que aprendí al hacer este programa:
#
# - Separé el código en funciones: agregar_producto(), mostrar_inventario() y calcular_estadisticas().
#   Esto ayuda a que el código sea más limpio, fácil de leer y mantener.
#
# - Cada producto se guarda como un diccionario con las claves:
#   "nombre", "cantidad", "precio" y "costo_total". Esto hace que los datos sean fáciles de manejar.
#
# - Todos los productos se almacenan en una lista llamada inventario1.
#   La lista funciona como historial de todos los productos ingresados.
#
# - Hice validaciones de datos para asegurarme de que:
#     * Los nombres solo tengan letras
#     * Las cantidades sean números enteros
#     * Los precios sean números decimales
#   Así evito errores al ejecutar el programa.
#
# - El menú se creó usando while True y if-elif-else para que el usuario pueda
#   elegir acciones varias veces hasta que decida salir.

    


    

