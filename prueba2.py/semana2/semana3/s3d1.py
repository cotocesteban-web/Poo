def mensaje_bienvenida ():
    print('Bienvenido al sistema de ventas\n Esperamos que tenga un buen dia. ')
   

def saludar_cliente(nombre):
    print(f'hola {nombre} , bienvenido al gimnacio.')

def calculo_total (precio ,  cantidad):
    pago= precio * cantidad
    return pago
def compra (dinero , cantidad)


def sala_videojuegos (compra):
    print('1 comprar fichas (si / no): ')
    print('2 salir.')
    if compra == 'si':
        nombre = input('Como te llamas: ')
        dinero = float(input('Cuanto de dinero tienes: '))
        fichas = 500
        cantidad = fichas / dinero
        resto = dinero - fichas
        if dinero > fichas:
             print ()

         

def menu ():
     print ('1 mensaje de bienvenida')
     print ('2 ')
     int(input(' selecione una opcion (1-4): '))

match menu:
     case 1:
        mensaje_bienvenida ()
    
    case 2:
        nombre = input ('ingrese su nombre: ')
        saludar_cliente (nombre)
  
    case 3:
            
    case 4:
    case _ :
         print ('opcion invalida.')

    
