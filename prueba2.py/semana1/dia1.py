#productoFavorito = input("como fue su experiencia en la tienda y cual fue su producto favorito ")
#print("su producto favorito fue: " + productoFavorito)
#puntuacion = input("cual fue nuesta atencion si la podrias calificar del 1 al 10 ")
#print("su producto favorito fue: " + puntuacion)
#print("gracias por su calificacion y esperamos que vuelva pronto ")


product1=input(" Indique el nombre del producto ")
precio1=input("indique el precio del producto ")
cantidad1=input("indique la cantidad ")

product2=input(" Indique el nombre del producto ")
precio2=input("indique el precio del producto ")
cantidad2=input("indique la cantidad ")

product3=input(" Indique el nombre del producto ")
precio3=input("indique el precio del producto ")
cantidad3=input("indique la cantidad ")


print("======================")
print("factura de la tienda")
print("======================")
# encabezado de la factura

print(f"{"Producto":10s}\t{"Precio":5s}\t{"Cantidad":5s}")
print(f"{product1:10s}\t{precio1:5s}\t{cantidad1:5s}")
print(f"{product2:10s}\t{precio2:5s}\t{cantidad2:5s}")
print(f"{product3:10s}\t{precio3:5s}\t{cantidad3:5s}")