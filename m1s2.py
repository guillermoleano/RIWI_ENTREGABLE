from utils import agregar_producto
from utils import mostrar_inventario
from utils import calcular_estadisticas
import os
inventario1 = []

def clear():
    os.system("cls" if os.name == "nt" else "clear")

while True:
    opcion = int(input("""Seleccione una de las siguientes opciones:
    1. Agregar producto
    2. Mostrar inventario
    3. Calcular estadísticas
    4. Salir

    Ingrese su opción: """))

    if opcion == 1:
        inventario1 = agregar_producto()
    if opcion == 2:
        clear()
        if not inventario1:  # validar si está vacío
            print("El inventario está vacío")
        else:
            mostrar_inventario(inventario1)  # mostrar la lista real
    if opcion == 3:
        clear()
        if not inventario1:  # validar si está vacío
            print("Estadisticas no disponibles. El inventario está vacío")
        else:
            calcular_estadisticas(inventario1) 
    if opcion == 4:
        print("salir")
        break

    

