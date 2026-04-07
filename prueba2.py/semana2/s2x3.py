# ===========================
# ejercicio 1
# =========================

print('')
print('Bienvenido a la plataforma del torneo juvenil.')
print('')

nombre= input('hola, podias indicar tu nombre: ')
edad = int(input('indica tu edad: '))
estatus = input('estas inscrito en el torneo (si / no) ')

print('hola validarenos tus datos y te diremos el estatus de tu inscripcion.')
if (edad >= 15) and ( estatus == 'si'):
    print(f'hola {nombre}')
    print('Bienvedo al torneo tu inscripcion fue exitosa.')
else:
    print(f'hola {nombre}')
    print('no cumples con los requisitos minimos para poder entrar al torneo.')


# ==============================
# ejercicio 2
# ==============================

bateria = int(input('ingrese el porcentaje de bateria '))

if (bateria <= 20):
    print('Debe cargar el celular.')
else:
    print('la bateria es suficiente.')

# =============================
# ejercicio 3
# ============================

print(' Bienvenido a rapienvios.')

paquete = float(input('hola podrias indicar el peso de tu paquete en kilogramos: '))

if (paquete < 1):
    print("tu paquete es liviano.")
elif (paquete >= 1) and (paquete <= 5):
    print('tu paquete es estandar.')
elif (paquete > 5):
    print('tu paquete es pesado')
print('gracias por utilizar nuestro servicio.')

#============================
# ejercicio 4
#==============================

color= input(' Ingrese el color del semaforo: ')

if color== 'verde':
    print('Avanzar')
elif color == 'amarillo':
    print('Precaucion.')
elif color == 'rojo':
    print('Detenerse.')
else:
    print('error en el sistema verifique color')

    
#==================================
# ejercicio 5
#=================================

print('Salas VIP GO.')

cliente = input('hola como te llamas: ')
edad = int(input('Que edad tienes. '))
entrada = input('Con que tipo de entrada cuentas (general o VIP) ')
efectivo = float(input('Con cuanto de dinero cuentas en este momento en tu cuenta: '))
precio = 250


if (entrada == 'VIP'):
    print(' Hola cuentas con etrada VIP pero tienes que tener 18 años para poder entrar. ')
    if (edad >= 18) and (entrada == "VIP"):
        print('Bienvenido cumples con los requisitos para entrar a la sala.')
        compra= input('deseas tomar una de nuestras bebidas especiales (si/no): ')
        if (compra == 'si') and ((efectivo - precio) > 0 ):
            print(' Compra aprobada.')
            print(f'tu cambio es de {efectivo - precio}')
        else:
            print(' No cuetas con los fondos suficientes.')
    else:
        print('tu acceso es denegado al area VIP.')


#===============================
# ejercio 6
#=============================
print('Sitio de becas gubernamentales.')
print('Bienvenido al sitio de becas.')

estudiante = input('Ingrese el monbre del aspirante: ')
promedio = int(input(' Indica tu promedio final en "%": '))
ingresos = float(input('cuales son tus ingresos familiares: '))
cursos = int(input("ingresa la cantidad de cursos aprobados. "))
beca = 100000
sin_beca = 0
beca_parcial = 0.5


if (promedio < 70):
    print(f"hola {estudiante}")
    print('tu beca no fue aprobada.')
    print(f"el monto resibido puede ser de Q. {beca*sin_beca}")
elif (promedio >= 70) and (promedio <= 84):
    print(f"hola {estudiante}")
    print('puedes resibir una beca parcial.')
    print(f"el monto resibido puede ser de Q. {beca*beca_parcial}")
elif (promedio > 84):
    if (cursos >= 5) and (ingresos <= 400000):
        print(f"hola {estudiante}")
        print('puedes resibir una beca completa.')
        print(f"el monto resibido puede ser de Q. {beca}")
    else:
        print(f"hola {estudiante}")
        print('puedes resibir una beca parcial.')
        print(f"el monto resibido puede ser de Q. {beca*beca_parcial}")  

#===========================
# ejercicio 7
#==========================

print(' hotel Grad. ')
print('Hola bienvenido al hotel Grad')

cliente = input(' bienvenido con quien tenemos el gusto: ')
temporada = input('en que temporada deseas resevar (alta-media-baja): ')
estadia = float(input('por cuanto tiempo nos visitas: '))
precio = 125
membresia = input(' cuentas con una membresia (si / no)')

match temporada:
    case "alta":
        recargo1 = (estadia * precio)*1.2
        if (membresia == 'si') and (estadia >= 3):
            descuento1 = recargo1*0.15
            print(cliente)
            print(f'el subtotal es Q {recargo1}')
            print(f'el descuento es Q. {recargo1*.15}')
            print(f'el total es Q. {recargo1-descuento1}')
        elif (membresia == 'si') or (estadia < 3 ):
            descuento2 = recargo1*0.15
            print(cliente)
            print(f'el subtotal es Q {recargo1}')
            print(f'el descuento es Q. {recargo1*.15}')
            print(f'el total es Q. {recargo1-descuento2}')
    
    case 'media':
        recargo2 = (estadia * precio)* 1.1
        if (membresia == 'si') and (estadia >= 3):
            descuento3 = recargo2*0.15
            print(cliente)
            print(f'el subtotal es Q {recargo2}')
            print(f'el descuento es Q. {recargo2*.15}')
            print(f'el total es Q. {recargo2-descuento3}')
        elif (membresia == 'si') or (estadia < 3 ):
            descuento4 = recargo1*0.15
            print(cliente)
            print(f'el subtotal es Q {recargo2}')
            print(f'el descuento es Q. {recargo2*.15}')
            print(f'el total es Q. {recargo2-descuento4}')
    case  'baja':
        recargo3 = (estadia * precio)
        if (membresia == 'si') and (estadia >= 3):
            descuento5 = recargo2*0.15
            print(cliente)
            print(f'el subtotal es Q {recargo3}')
            print(f'el descuento es Q. {recargo3*.15}')
            print(f'el total es Q. {recargo3-descuento5}')
        elif (membresia == 'si') or (estadia < 3 ):
            descuento6 = recargo3*0.15
            print(cliente)
            print(f'el subtotal es Q {recargo3}')
            print(f'el descuento es Q. {recargo3*.15}')
            print(f'el total es Q. {recargo3-descuento6}')
    

#=============================
# ejercicio 8
#===============================

print("Academia Flot:")
print("1 o matricula ")
print("2 o notas")
print("3 o certificado")
print("4 o salir")

opcion = input("Seleccione (1-4) o escriba matricula - notas - certificado - salir ")
usuario = input("Ingrese su nombre de usuario (admin, profesor, estudiante): ")
promedio = float(input("indique su promedio"))

match opcion:

    case ("matricula" | "1") if usuario == "admin" or usuario == "profesor":
        print("matriculado. ")
    
    case "nota" | "2" if usuario == "estudiante" or usuario == "profesor":
        print("Notas del curso. ")

    case "salir" | "3" if usuario == "estudiante" and promedio >= 70:
        print("se genero su sertificado. ")

    case "salir "| "4" :
        print("fin del programa. ")
    case _:
        print("error del sistema ingrese nuevamente los datos")

#========================
# ejercicio 9
#===========================

