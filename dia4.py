# manejo de archivosÑ

## ls programs sufren de amnecia cuando se apaga la memoria se pierdde solo viven en l amemoria ram
#  interactuando con los archivos
#  metodos de apertura
# "open"

# modos ade apertura:
# modo w = 
# write / escribir: crea un archivo nuevo
# advertencia si el archivo ya existia el modo W lo destruye y lo sobreescribe desde 0

# modo 2:
# modo "a" = append/aniadir: 
# abre un archivo exixtente y coloca el cursosr al final.
# todo lo que escribamos se agrega sin borrar lo anterior


# 0modo "r":
# solo nos permite ver el contenido no podemos modificar o agregar
# si el archivo no existe, el program se detendra con un error.

# simpre que se abra un archovo hay que cerrarlo

# para escribir en mi archivo usamos la funcion write

# archivo_prueba = open("archivo.txt", "a")
# archivo_prueba.write("hoy aprendi a escribir em um archivo\n")
# archivo_prueba.write("hoy aprendi a escribir em um archivo\n")
# archivo_prueba.close()

### forma Simplificado de abrir y cerrar
# administrador de contexto "whit open"

# with open("archivo.tx", "a") as archivp_prueba:
#     archivo_prueba.write("hoy aprendi a escribir em um archivo\n")
#     archivo_prueba.write("hoy aprendi a escribir em um archivo\n")


## leeer nuestro archivo
# with open("archivo.tx", "r") as archivo_prueba:
#     print("contenido del archivo")
#     for linea in archivo_prueba:
#         # funcion strip() Elimina los espacios en blanco y los saltos de linea
#         texto_limpio = linea.strip()
#         print(f"{texto_limpio}")

with open("registro.txt", "r") as archivo_prueba:
    contador = 0
    for linea in archivo_prueba:
        texto_limpio = linea.strip()
        contador += 1
        print(f"{texto_limpio}")

print(f"total de lineas es: {contador}")

### el methodo "reaf()"

# whit open("cuento.txt, "r")as archivo_prube