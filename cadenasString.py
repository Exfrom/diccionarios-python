#METODOS DE ANALISIS
#count()retorna el número de veces que se repite un conjunto de caracteres especificado.
s = "hola mundo"
print(s.count("hola"))
print(s.count("mundo"))
print(s.count("mundo", 1))
print(s.count("mundo", 10))

#find() etornan la ubicación (comenzando desde el cero) en la que se encuentra el argumento indicado.
s = "hola mundo"
print(s.find("hola"))
print(s.find("mundo"))
print(s.find("mundo", 1))
print(s.find("mundo", 10))

#index()retornan la ubicación (comenzando desde el cero) en la que se encuentra el argumento indicado.
s = "hola mundo"
print(s.index("hola"))
print(s.index("mundo"))
print(s.index("mundo", 1))
 

#ValueError
#print(s.index("world"))

#rfind() y rindex()
s = "C:/python36/python.exe"
print (s.find("/"))
print (s.rfind("/"))

s = "Hola mundo"
print(s.startswith("Hola"))
print(s.endswith("mundo"))

print(s.endswith("world"))
#isdigit(), isnumeric()
print ("1234".isnumeric())
print ("1234".isdecimal())

print("abc123".isdigit())
# Determina si todos los caracteres son alfanuméricos.
print("abc123".isalnum())
# Determina si todos los caracteres son alfabéticos.
print("abcdef".isalpha())
print("abc123".isalpha())
# Determina si todas las letras son minúsculas.

print( "abcdef".islower())
#mayuscula
print("ABCDEF".isupper())
# Determina si la cadena contiene todos caracteres imprimibles.
print("Hola \t mundo!".isprintable())

# Determina si la cadena contiene solo espacios.
print("Hola mundo".isspace())
print("    ".isspace())
#METODOS DE  TRANSFORMACION

#capitalize() retorna la cadena con su primera letra en mayúscula.
print("hola mundo".capitalize())
#encode() codifica la cadena con el mapa de caracteres especificado y retorna una instancia del tipo bytes.
print("Hola mundo".encode("utf-8"))
#center(), ljust() y rjust
print("Hola".center(10))
print("Hola".ljust(10))
print("Hola".rjust(10))

#Estos métodos son especialmente útiles al imprimir en forma de tabla para que ésta se mantenga alineada. Un segundo argumento indica con qué caracter se deben llenar los espacios vacíos (por defecto un espacio en blanco).
print("Hola".center(10, "*"))

#lower() y upper() retornan una copia de la cadena con todas sus letras en minúsculas o mayúsculas según corresponda.
print("Hola Mundo!".lower())
print("Hola Mundo!".upper())
#swapcase(), por su parte, cambia las mayúsculas por minúsculas y viceversa.
print("Hola Mundo!".swapcase())

#Las funciones strip(), lstrip() y rstrip() remueven los espacios en blanco que preceden y/o suceden a la cadena.
s = " Hola mundo! "
print(s.strip())
# Remueve los de la derecha.
print(s.rstrip())
# Remueve los de la izquierda.
print(s.lstrip())
#Por último, el método replace() ─ampliamente utilizado─ reemplaza una cadena por otra.
s = "Hola mundo"
print(s.replace("mundo", "world"))


#METODOS DE SEPARACION Y UNION

#El método de división de una cadena según un caracter separador más empleado es split(), cuyo separador por defecto son espacios en blanco y saltos de línea.
print ("Hola mundo!\nHello world!".split())
#El separador puede indicarse como argumento.
print("Hola mundo!\n Hello world!".split(" "))
#O bien, para separar únicamente según saltos de línea:
print("Hola mundo!\nHello world!".splitlines())
#Un segundo argumento en split() indica cuál es el máximo de divisiones que puede tener lugar (-1 por defecto para representar una cantidad ilimitada).
print("Hola mundo hello world".split(" ", 2))
#Un segundo método de separación es partition(), que retorna una tupla de tres elementos: el bloque de caracteres anterior a la primera ocurrencia del separador, el separador mismo, y el bloque posterior.
s = "Hola mundo. Hello world!"
print(s.partition(" "))
#rpartition() opera de forma similar, pero realizando la búsqueda de derecha a izquierda.
print(s.rpartition(" "))
#Por último, el método join() ─sumamente útil─, que debe ser llamado desde una cadena que actúa como separador para unir dentro de una misma cadena resultante los elementos de una lista.
print(" ".join(["Hola", "mundo"]))
print(", ".join(["C", "C++", "Python", "Java"]))