persona = {
    "firstname": "Diana Shirley",
    "lastname": "Celis Bautista",
    "age": 38,
    "id":1073160285,
    "state":True
}

#MOSTRAR DICCIONARIO
print(persona)
print(persona["firstname"])
print(persona.get("lastname"))

#mMODIFICAR DICCIONARIO

persona["firstname"]="Tatiana Lisbeth"
print(persona["firstname"])
#agregar un nuevo key con su valor
persona["Title"]="Ingeniera de Software"
print(persona["Title"])
#accede la diccionario para modificar su valor
persona.update({"firstname":"Diana Shirley"})
print(persona)

#BORRAR ELEMENTOS
#borra por un key
persona.pop("Title")
print(persona)
#borra el ultimo elemento
persona.popitem()
print(persona)

del persona["firstname"]
print(persona)

#persona.clear("lastname")
#print(persona)

#mostrar los key
for m in persona:
    print(m)

for m in persona:
    print(persona[m])

for k,m in persona.items():
    print(k,":", m)


