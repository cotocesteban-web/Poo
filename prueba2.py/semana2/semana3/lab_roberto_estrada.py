lista_invitados = []

def agregar_invitados (nombre , lista_nueva):
    lista_nueva .append (nombre)
    return lista_nueva

def mostrar_lista (Lista_invitados):
    for nombre in lista_invitados:
        print (f'Nombre: {nombre}')


def buscar_invitado (nombre , lista_invitados):
    if nombre in lista_invitados:
        print ('El invitado ya está en la lista.')

    else:
        print ('Nombre disponible.')


def eliminar_invitado (nombre , lista_invitados):
    if buscar_invitado (nombre):
        lista_invitados .remove(nombre)
        print('El nombre fue eliminado de la lista exitosamente. ')

    else:
        print ('Nombre inexistente.')

def menu (lista_invitados):
    print("1. Bienvenido.")
    print("2. Registrar nuevo invitado.")
    print("3. ver lista completra.")
    print("4. eliminar invitado. ")
    print("5. salir.")

    while True:
        opcion = int(input('seleciona una opcion valida: '))

        match opcion:

            case 1:
                print('Bienvenido al sistema.')

            case 2:
                nombre = input("Ingrese el nombre del invitado: ")
                lista_invitados = agregar_invitados(nombre, lista_invitados)
                print('registrando.')
            case 3:
                mostrar_lista(lista_invitados)

            case 4:
                nombre = input('Ingrese el nombre de la persona a eliminar: ')
                eliminar_invitado(nombre , lista_invitados)

            case 5:
                print('salindo del sistema... ')
                break

            case _:
                print('error en la digitacion de los datos vuelva a intentar.')
                
menu(lista_invitados)


