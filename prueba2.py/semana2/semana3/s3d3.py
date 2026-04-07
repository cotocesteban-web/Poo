# ejercicio 1. tienda de frutas.
print ('Tienda de frutas.')

inventario = [
    [10, 4, 8],
    [5, 12, 3],
    [7, 20, 6]
]

frutas_total = 0

for lista in inventario:
    for cantidad in lista:
        if cantidad > 5 and cantidad % 2 == 0:
            frutas_total += cantidad

print ('Inventario total: ', frutas_total,'.')

#ejercicio 2 tienda de abarrotes
print ('Tienda de abarrotes.')

precios_pasillos = [
    [10.0, 55.0, 20.0],
    [45.0, 80.0, 12.0],
    [100.0, 30.0, 48.0]
]

porcentaje = 0.10

for lista in range (len (precios_pasillos)):
    for producto in range (len(precios_pasillos[lista])):
        if precios_pasillos [lista] [producto] < 50:
            precios_pasillos [lista] [producto] += precios_pasillos [lista] [producto] * porcentaje

print (' Precios actualizados. ')
for fila in precios_pasillos:
    print (fila)
