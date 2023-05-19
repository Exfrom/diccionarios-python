fruver = []
while True:
    print("Fruver supermercado Noe")
    print("1.Anadir/modificar")
    print("2.Buscar")
    print("3.Borrar")
    print("4.Listar")
    print("5.Salir")
    opcion= int(input("Que opcion desea realizar?:"))
    if (opcion == 1):
        articulo=input("Ingrese el nombre del articulo: ")
        if articulo in fruver:
            print("El articulo ya se encuentra registrado!")

            
            modificar = input("1.Modificar precio del articulo \n" "2.modificar tipo de articulo \n" "3.Terminar")
            if modificar == "1" :
                precio = int(input("Ingrese el precio del articulo: "))
                fruver[articulo]['precio']= precio
                print("Articulo Agregado!")
            elif modificar == "2":
                tipo = int(input("Ingrese el nuevo tipo de articulo 1. vegetal 2. Fruta"))
                if (tipo == 1):
                    variedad="vegetal"
                elif(tipo == 2):
                    variedad="fruta"
                fruver[articulo]['tipo']=variedad
                print("articulo modificado")
        else:
            #fruver[articulo]={}
            precio =int(input("Ingrese el nuevo precio del articulo"))
            fruver[articulo]['precio']=precio
            tipo =int(input("Seleccione el tipo de articulo 1. vegetal 2.fruta \n"))
            if (tipo == 1):
                variedad="vegetal"
            elif (tipo == 2):
                variedad="fruta"
            fruver[articulo]['tipo']=variedad
            print(fruver)
    elif (opcion == 2):
        texto = input("¿Cual es el articulo a buscar?:")
        print("se encotraron los siguientes articulos")
        for articulo,dato in fruver.items():
            if articulo.startswith(texto):
                print(f"El precio del articulo ingresado es: {fruver[articulo]['precio']}")
                print(f"el tipo de articulo ingresado es: {fruver[articulo]['tipo']}")
                #print(articulo)
    elif (opcion == 3):
        articulo = input("¿Cual es el articulo a borrar?_")
        if articulo in fruver:
            del fruver[articulo]
            print(f"El articulo {articulo} fue borrado")
        else:
            print("El articulo no existe!")

    elif (opcion == 5):
        print("saliendo del programa ... ¡Adios!")
        break
    

