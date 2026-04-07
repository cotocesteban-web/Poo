print('Inventario de la tienda ')
print('')
cantidad_leche=int(input('Bienvenido podria indicar la cantidad de leche que se tiene en existencia. '))
print('')

if (cantidad_leche > 20):
    print('inventario saludable')
elif (cantidad_leche >= 1) and (cantidad_leche <= 20):
    print('Alerta: hacer pedido al proveedor. ')
elif (cantidad_leche == 0):
        print('Urgente: producto agotado. ')




