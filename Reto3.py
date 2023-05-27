instructores2557861 = {}

while True:
    print("Agenda de Instructores")
    print("1. Agregar/Modificar")
    print("2. Buscar")
    print("3. Borrar")
    print("4. Listar")
    print("5. Salir")

    opcion = int(input("¿Qué opción desea realizar?: "))

    if opcion == 1:
        nombre = input("Ingrese el nombre del instructor: ")
        
        if nombre in instructores2557861:
            print(f"Instructor: {nombre}")
            print(f"Materia: {instructores2557861[nombre]['materia']}")
            print(f"Teléfono: {instructores2557861[nombre]['telefono']}")
            
            modificar = input("¿Desea modificar los datos? (s/n): ")
            if modificar.lower() == "s":
                materia = input("Ingrese la materia: ")
                telefono = input("Ingrese el teléfono: ")
                instructores2557861[nombre]['materia'] = materia
                instructores2557861[nombre]['telefono'] = telefono
                print("Datos del instructor modificados correctamente.")

        else:
            materia = input("Ingrese la materia: ")
            telefono = input("Ingrese el teléfono: ")
            instructores2557861[nombre] = {'materia': materia, 'telefono': telefono}
            print("Instructor agregado correctamente.")

    elif opcion == 2:
        texto = input("Ingrese un texto de búsqueda: ")
        encontrados = []

        for nombre, datos in instructores2557861.items():
            if nombre.startswith(texto):
                encontrados.append(nombre)

        if len(encontrados) > 0:
            print("Instructores encontrados:")
            for nombre in encontrados:
                print(f"Instructor: {nombre}")
                print(f"Materia: {instructores2557861[nombre]['materia']}")
                print(f"Teléfono: {instructores2557861[nombre]['telefono']}")
                print("--------------")
        else:
            print("No se encontraron instructores con ese nombre.")

    elif opcion == 3:
        nombre = input("Ingrese el nombre del instructor a borrar: ")

        if nombre in instructores2557861:
            borrar = input(f"¿Está seguro de que desea borrar a '{nombre}'? (s/n): ")
            if borrar.lower() == "s":
                del instructores2557861[nombre]
                print("Instructor borrado correctamente.")
        else:
            print("El instructor no existe en la agenda.")

    elif opcion == 4:
        print("Lista de instructores:")
        if len(instructores2557861) > 0:
            for nombre, datos in instructores2557861.items():
                print(f"Instructor: {nombre}")
                print(f"Materia: {datos['materia']}")
                print(f"Teléfono: {datos['telefono']}")
                print("--------------")
        else:
            print("La agenda de instructores está vacía.")

    elif opcion == 5:
        print("Saliendo del programa... ¡Adiós!")
        break

    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")