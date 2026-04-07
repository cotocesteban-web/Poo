print(' Bienvenido al laboratorio 3D.')

estudiante = input("Nombre: ")
edad = int(input('Edad del estudiante: '))
autorizacion = input(' Tienes autorizado entrar (si/no): ')
saldo = float(input('indica tu saldo actual: '))
paquete = float(input(' indica el paquete que deseas adquirir: '))

if edad >= 15 and autorizacion == "si":
    contador = 0
    print("Acceso concedido al laboratorio 3D" , estudiante)
    while saldo >= paquete:
        compra = input('Deseas comprar minutos extra en el laboratorio (si/no) ? ')
        if compra == 'si':
            saldo -= paquete
            contador += 1
        else:
            break


    print('Compra aprobada.')
    print('paquete compraado: ', contador)
    print ('saldo actual: ', saldo)
else:
    print("Tu acceso fue denegado a la sala de imprecion 3D.")