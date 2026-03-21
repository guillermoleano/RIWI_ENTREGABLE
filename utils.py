# Lista global donde se almacenan los productos
inventario = []  # Lista para almacenar los productos del inventario y se define afuera para que empiece en 0

def agregar_producto():
    
    # Variables iniciales (no es necesario definir tipo aquí, pero lo dejas como guía)
    nombre = str
    cantidad = int
    precio = float
    # Validación del nombre (solo letras y espacios)
    while True: 
        nombre = input("Ingrese nombre del producto: ")  
        if nombre.replace(" ", "").isalpha(): 
            break 
        else: 
            print("Debe ingresar un nombre valido.") 
        
    # Validación de la cantidad (solo números enteros)    
    while True: 
        cantidad = input("Ingrese cantidad: ")
        if cantidad.isdigit():
            cantidad = int(cantidad) #Convertir la cantidad a entero
            break
        else:
            print("Debe ingresar un numero valido.")
    # Validación del precio (número decimal)    
    while True:
        try:
            precio = float(input("Ingrese precio: "))
            break
        except ValueError:
            print("Debe ingresar un numero valido.")
    # Cálculo del costo total del producto
    costo_total = cantidad * precio
    # Creamos un diccionario con los datos del producto
    producto = {
                "nombre": nombre,
                "precio": precio,
                "cantidad":cantidad,
                "costo_total":costo_total,
                }   
    # Agregamos el producto al inventario
    inventario.append(producto)
    # Retornamos la lista actualizada
    return inventario

def mostrar_inventario(inventario1):
    # Encabezado de la tabla
    print(f"{'Nombre':<10} {'Precio':<10} {'Cantidad':<10}")
    print("-" * 30)
    # Recorremos cada producto en la lista
    for p in inventario1:
        nombre = p["nombre"]
        precio = p["precio"]
        cantidad = p["cantidad"]
        # Mostramos cada producto formateado
        print(f"{nombre:<10} ${precio:<9} {cantidad:<10}")

def calcular_estadisticas(inventario1):
        # Suma total de cantidades
    total_cantidad = sum(p["cantidad"] for p in inventario1)
    print("Cantidad total de todos los productos:", total_cantidad)
    valor_total_del_inventario = sum(p["costo_total"] for p in inventario1)
    print("El valor total del inventario es:", valor_total_del_inventario)
    


    
