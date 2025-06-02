def agregar_producto(productos): #Función para agregar un producto a la lista. 
    while True:
        while True:
            nombre = input("Nombre del producto: ").strip()
            if not nombre:
                print("❌ Ingrese un nombre para el producto.") #Verifico que el nombre no esté vacio.
            elif not nombre.replace(" ", "").isalpha():
                print("❌ Ingrese un nombre valido para el producto.") #Verifico que el nombre sea solo letras.
            else:
                break
        while True:
            categoria = input("Categoría: ").strip()
            if not categoria:
                print("❌ Ingrese una categoría para el producto.") #Verifico que la categoria no esté vacia.
            elif not categoria.replace(" ", "").isalpha():
                print("❌ Ingrese una categoria valida para el producto.") #Verifico que la categoria sea solo letras.
            else:
                break
        while True:
            try:
                precio = int(input("Precio: $"))
            except ValueError: #Verifico que el precio sea un número entero positivo. Use una excepción para manejar errores. ¿Debo utilizarlas?
                print("❌ Ingrese un precio válido")
            else:
                if precio <= 0:
                    print("❌ El precio debe ser un número positivo.")
                else:
                    break
        duplicado = False #Verifico si el producto ya existe (¿Debo verificar categoria?, en esta entrega la verifico)
        for prod in productos:
            if nombre.strip().lower() == prod[0].strip().lower() and categoria.strip().lower() == prod[1].strip().lower():
                duplicado = True
                break
        if duplicado:
            print("❌ Ya existe un producto con ese nombre y categoría.")
            continue
        producto = [nombre, categoria, precio]
        productos.append(producto)
        print(f"✅ El producto '{nombre}' fue agregado correctamente.")
        while True:
            continuar = input("¿Desea agregar otro producto? (si/no): ").lower()
            if continuar == 'si' or continuar == 'no':
                break
            else:
                print("❌ Respuesta inválida. Por favor, ingrese 'si' o 'no'.")
        if continuar != 'si':
            break

def ver_productos(productos): #Función para mostrar la lista de productos.
    print("LISTA DE PRODUCTOS")
    if not productos: #Verifico si la lista de productos está vacia.
        print("No hay productos cargados.")
    else:
        for i, producto in enumerate(productos, 1):
            nombre, categoria, precio = producto
            print(f"{i}. {nombre} | Categoría: {categoria} | Precio: ${precio}")

def buscar_producto(productos): #Función para buscar un producto por nombre o categoría.
    print("BUSCAR PRODUCTO")
    if not productos: #Verifico si la lista de productos está vacia.
        print("No hay productos cargados.")
        return
    while True: 
        busqueda = input("Ingrese nombre o categoría (o 'cancelar' para volver): ").lower()
        if busqueda == 'cancelar':
            print("Búsqueda cancelada.")
            break
        elif not busqueda.replace(" ", "").isalpha(): #Verifico que la entrada sea solo letras.
            print("❌ Ingrese un nombre o categoría válido (solo letras).")
            continue
        resultados = []
        for producto in productos:
            nombre, categoria, precio = producto
            if busqueda in nombre.lower() or busqueda in categoria.lower():
                resultados.append(producto)
        if resultados:
            print("Resultados encontrados:")
            for i, producto in enumerate(resultados, 1):
                nombre, categoria, precio = producto
                print(f"{i}. {nombre} | Categoría: {categoria} | Precio: ${precio}")
        else:
            print("❌ No se encontraron productos.")

def eliminar_producto(productos): #Función para eliminar un producto de la lista.
    ver_productos(productos)
    if not productos: #Verifico si la lista de productos está vacia.
        return 
    while True:
        entrada = input("Ingrese el número del producto a eliminar (o 'cancelar' para volver): ")
        if entrada.lower() == 'cancelar':
            print("Operación cancelada.")
            break
        try:
            indice = int(entrada) - 1
            if 0 <= indice < len(productos):
                producto_eliminado = productos.pop(indice)
                print(f"❌ Producto '{producto_eliminado[0]}' eliminado.")
                break
            else:
                print("❌ Número inválido. Intente nuevamente.") #Verifico que el número ingresado sea válido.
        except ValueError: #Verifico que la entrada sea un número entero con el ValueError. Para esta entrega, las uso
            print("❌ Error: Ingrese un número válido o 'cancelar'.")

productos = [] 

while True: # Menu principal del sistema. ¿Podria usar una función para el menu?
    print("\n Sistema de Gestion Basica De Productos")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    opcion = input("Seleccione una opcion: ")
    
    if opcion == "1":
        agregar_producto(productos)
    elif opcion == "2":
        ver_productos(productos)
    elif opcion == "3":
        buscar_producto(productos)
    elif opcion == "4":
        eliminar_producto(productos)
    elif opcion == "5":
        break
    else:
        print("❌ Opción Inexistente. Vuelva a intentarlo.")