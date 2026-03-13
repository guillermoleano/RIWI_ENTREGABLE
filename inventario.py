

#Aqui se definen las variables para el nombre del producto, la cantidad y el precio, se asignan los tipos de datos correspondientes a cada variable. 
nombre = str
cantidad = int
precio = float
#Aqui atraves de un ciclo while se valida que el nombre del producto solo contenga letras 
#y espacios, si el nombre es valido se sale del ciclo, de lo contrario se muestra un mensaje de error y se vuelve a pedir el nombre
while True: 
    nombre = input("Ingrese nombre del producto: ")  
    if nombre.replace(" ", "").isalpha(): 
        break 
    else: 
        print("Debe ingresar un nombre valido.") 
    break
#Aqui se valida que la cantidad ingresada sea un numero, si es valido se sale del ciclo, de lo contrario se 
#muestra un mensaje de error y se vuelve a pedir el precio. Por medio del try except se maneja la excepcion 
#de que el usuario ingrese un valor no numerico, si el valor es valido se sale del ciclo, de lo contrario se muestra un mensaje de error y se vuelve a pedir el precio.  
while True:
    try:
        precio = float(input("Ingrese precio: "))
        break
    except ValueError:
        print("Debe ingresar un numero valido.")

#Aqui se valida que la cantidad ingresada sea un numero entero, si es valido se sale del ciclo, de lo contrario se muestra
while True: 
    cantidad = input("Ingrese cantidad: ")
    if cantidad.isdigit():
        cantidad = int(cantidad) #Convertir la cantidad a entero
        break
    else:
        print("Debe ingresar un numero valido.")

#Aqui se calcula el costo total multiplicando el precio por la cantidad y se muestra un mensaje
#con el nombre del producto, el precio, la cantidad y el costo total.
costo_total = precio * cantidad
print(f"Producto: {nombre} / Precio: {precio} / Cantidad: {cantidad} / Total: {costo_total}") 

#Explicacion general del codigo: Este codigo es un programa de inventario que permite al usuario ingresar 
# el nombre de un producto, su precio y la cantidad disponible. El programa valida que el nombre del producto solo 
# contenga letras y espacios, que el precio sea un numero valido y que la cantidad sea un numero entero. Luego, calcula 
# el costo total multiplicando el precio por la cantidad y muestra un mensaje con los detalles del producto y el costo total.
