fruver = {}

while True:
    print("Fruver supermercado Noe")
    print("1. Añadir/modificar")
    print("2. Buscar")
    print("3. Borrar")
    print("4. Listar")
    print("5. Salir")

    opcion = int(input("¿Qué opción desea realizar?: "))

    if opcion == 1:
        articulo = input("Ingrese el nombre del artículo: ")
        
        if articulo in fruver:
            print("El artículo ya se encuentra registrado!")
            
            modificar = input("1. Modificar precio del artículo\n2. Modificar tipo de artículo\n3. Terminar\n")
            
            if modificar == "1":
                precio = int(input("Ingrese el precio del artículo: "))
                fruver[articulo]['precio'] = precio
                print("Precio del artículo modificado.")
                
            elif modificar == "2":
                tipo = int(input("Ingrese el nuevo tipo de artículo (1. vegetal, 2. fruta): "))
                
                if tipo == 1:
                    variedad = "vegetal"
                elif tipo == 2:
                    variedad = "fruta"
                
                fruver[articulo]['tipo'] = variedad
                print("Tipo de artículo modificado.")
                
        else:
            fruver[articulo] = {}
            precio = int(input("Ingrese el precio del artículo: "))
            fruver[articulo]['precio'] = precio
            tipo = int(input("Seleccione el tipo de artículo (1. vegetal, 2. fruta): "))
            
            if tipo == 1:
                variedad = "vegetal"
            elif tipo == 2:
                variedad = "fruta"
            
            fruver[articulo]['tipo'] = variedad
            print("Artículo añadido correctamente.")

    elif opcion == 2:
        texto = input("¿Cuál es el artículo a buscar?: ")
        encontrado = False
        
        for articulo, datos in fruver.items():
            if articulo.startswith(texto):
                print(f"El precio del artículo '{articulo}' es: {datos['precio']}")
                print(f"El tipo de artículo es: {datos['tipo']}")
                encontrado = True
        
        if not encontrado:
            print("No se encontraron artículos con ese nombre.")

    elif opcion == 3:
        articulo = input("¿Cuál es el artículo a borrar?: ")
        
        if articulo in fruver:
            del fruver[articulo]
            print(f"El artículo '{articulo}' ha sido borrado.")
        else:
            print("El artículo no existe en la lista.")

    elif opcion == 4:
        print("Lista de artículos:")
        
        if len(fruver) > 0:
            for articulo, datos in fruver.items():
                print(f"Artículo: {articulo}")
                print(f"Precio: {datos['precio']}")
                print(f"Tipo: {datos['tipo']}")
                print("--------------")
        else:
            print("La lista de frutas está vacía.")

    elif opcion == 5:
        print("Saliendo del programa... ¡Adiós!")
        break

    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

