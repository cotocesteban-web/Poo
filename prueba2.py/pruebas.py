print ("Huellitas Felices")

inventario = [
["Croquetas",15, 20, 0],
["Juguete", 10, 5, 0],
["Champu",5, 12, 0]
]

def total_invertido (venta):
   return venta [1] * venta [2]


def resumen_entrada ():
   invercion_total = 0

   for lista in range(len(inventario)):
      subtotal = total_invertido(inventario)
      total_productos= total_inventario[lista]
      inventario[lista][3]=total_productos
      invercion_total += total_productos
      print (f"producto: {inventario[lista][0]}   | total Q {total_productos}")


print("                        ")
print (f"La invercion total es: Q", {inve})
print("                        ")


while True:
   print ("                         ")
   print ("Productos disponibles.")
   print('                          ')


   opciones= input ("Que desea hacer? (1. Vender /2.  agregar /3.  eliminar /4. salir):  ")
   if opciones == "1":
      producto = input("ingrese el nombre del Producto: ")
      for lista in inventario:
         if lista [0] == producto:
            cantidad = int((input("Indique la cantidad a comprar: ")))
            if lista[1] <= cantidad:
               lista[1] -= cantidad
               print ("venta realizada.")
            elif lista[1] > cantidad:
               print ("error cantidad insuficiente en inventario. ")
               cantidad =int(input("ingrese de nuevo la cantidad que desea comprar: "))
               break

   elif opciones == "2":
      nuevo_producto = input("ingrese el nuevo producto: ")
      cantidad = int(input("ingrese la cantidad de productos nuevos: "))
      precio = float(input("Cual es el precio del producto: "))
      inventario. append ([nombre, cantidad, producto, total])

   elif opciones == "3":
      eliminar_producto = input ("Ingrese el nombre del producto: ")
      for linea in range(len(inventario)):
         if eliminar_producto != inventario[linea][0]:
            print ("el producto no existe en el inventario.")
         elif eliminar_producto == inventario [linea][0]:
            inventario .pop(linea)
            print(f"'{eliminar_producto}' fue eliminado del inventario. ")
            break

   elif opciones == "4":
      resumen_entrada ()
      break
