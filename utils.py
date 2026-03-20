inventario = []  # Lista para almacenar los productos del inventario y se define afuera para que empiece en 0

def agregar_producto():
    
    
    nombre = str
    cantidad = int
    precio = float
    while True: 
        nombre = input("Ingrese nombre del producto: ")  
        if nombre.replace(" ", "").isalpha(): 
            break 
        else: 
            print("Debe ingresar un nombre valido.") 
        
    
    while True: 
        cantidad = input("Ingrese cantidad: ")
        if cantidad.isdigit():
            cantidad = int(cantidad) #Convertir la cantidad a entero
            break
        else:
            print("Debe ingresar un numero valido.")
    
    while True:
        try:
            precio = float(input("Ingrese precio: "))
            break
        except ValueError:
            print("Debe ingresar un numero valido.")
    costo_total = cantidad * precio
    producto = {
                "nombre": nombre,
                "precio": precio,
                "cantidad":cantidad,
                "costo_total":costo_total,
                }   
    inventario.append(producto)

    return inventario

def mostrar_inventario(inventario1):
    print(f"{'Nombre':<10} {'Precio':<10} {'Cantidad':<10}")
    print("-" * 30)

    for p in inventario1:
        nombre = p["nombre"]
        precio = p["precio"]
        cantidad = p["cantidad"]

        print(f"{nombre:<10} ${precio:<9} {cantidad:<10}")

def calcular_estadisticas(inventario1):
    total_cantidad = sum(p["cantidad"] for p in inventario1)
    print("Cantidad total de todos los productos:", total_cantidad)
    valor_total_del_inventario = sum(p["costo_total"] for p in inventario1)
    print("El valor total del inventario es:", valor_total_del_inventario)
    