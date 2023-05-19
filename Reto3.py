instructores2557861 = {}

def agregar_modificar():
    nombre = input("Ingrese el nombre del instructor: ")
    if nombre in instructores2557861:
        print("Nombre:", nombre)
        print("Materia:", instructores2557861[nombre]["materia"])
        print("Teléfono:", instructores2557861[nombre]["telefono"])
        modificar = input("¿Desea modificar la materia o el teléfono? (s/n): ")
        if modificar.lower() == "s":
            materia = input("Ingrese la materia que dicta el instructor: ")
            telefono = input("Ingrese el número de teléfono del instructor: ")
            instructores2557861[nombre]["materia"] = materia
            instructores2557861[nombre]["telefono"] = telefono
            print("Los datos del instructor han sido actualizados.")
    else:
        materia = input("Ingrese la materia que dicta el instructor: ")
        telefono = input("Ingrese el número de teléfono del instructor: ")
        instructores2557861[nombre] = {"materia": materia, "telefono": telefono}
        print("El instructor ha sido agregado a la lista.")

def buscar():
    texto_busqueda = input("Ingrese el texto de búsqueda: ")
    for nombre in instructores2557861:
        if nombre.lower().startswith(texto_busqueda.lower()):
            print("Nombre:", nombre)
            print("Materia:", instructores2557861[nombre]["materia"])
            print("Teléfono:", instructores2557861[nombre]["telefono"])

def borrar():
    nombre = input("Ingrese el nombre del instructor que desea borrar: ")
    if nombre in instructores2557861:
        confirmar = input("¿Está seguro que desea borrar a {} de la agenda? (s/n): ".format(nombre))
        if confirmar.lower() == "s":
            del instructores2557861[nombre]
            print("El instructor ha sido eliminado de la lista.")
    else:
        print("El instructor no se encuentra en la lista.")

def listar():
    print("Lista de instructores:")
    for nombre in instructores2557861:
        print("Nombre:", nombre)
        print("Materia:", instructores2557861[nombre]["materia"])
        print("Teléfono:", instructores2557861[nombre]["telefono"])
        print()

while True:
    print("\nMenú:")
    print("1. Agregar/Modificar")
    print("2. Buscar")
    print("3. Borrar")
    print("4. Listar")
    print("5. Salir")
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        agregar_modificar()
    elif opcion == "2":
        buscar()
    elif opcion == "3":
        borrar()
    elif opcion == "4":
        listar()
    elif opcion == "5":
        print("Saliendo del programa... Adios!")
        break
    else:
        print("Opción inválida.")