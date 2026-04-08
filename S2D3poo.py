# class Temperatura:
#     def __init__(self):
#         self.__grados = 20
#         self.__estado = "soleado"

#     @property
#     def grados(self): # equivalente al método get_grados()
#         return self.__grados

#     @grados.setter
#     def grados(self, nuevo_grado): # equivalente al método set_grados()
#         if nuevo_grado < 0:
#             print("Temperatura inválida")
#         else:
#             self.__grados = nuevo_grado

#     @property
#     def estado(self):
#         return self.__estado
    
#     @estado.setter
#     def estado(self, nuevo_estado):
#         self.__estado = nuevo_estado

# clima = Temperatura()
# # con el método traidicional, necesitamos usar el clima.get_grados() para obtener el valor de grados
# # clima.__grados NO FUNCIONA

# print(clima.grados)
# clima.grados = 50
# print(clima.grados)




# class Tienda:
#     # atributo de la clase(APLICA A TODOS)
#     impuesto_iva = 0.13

#     def __init__(self, productos):
#         self.productos = productos 

#     @classmethod
#     def cambiar_impuesto(cls, nuevo_impuesto):
#         cls.impuesto_iva = nuevo_impuesto

# Tienda.cambiar_impuesto(0.15)



# class RegistroVisitantes:
#     # atributo de clase: el total o contador de personas
#     total_personas = 0

#     def __init__(self, nombre_visitante):
#         self.nombre = nombre_visitante

#         # self.total_personas = 1 error comun

#         RegistroVisitantes.total_personas += 1
#         # RegistroVisitantes.total_personas = RegistroVisitantes.total_personas + 1 equivalente a la línea de arriba

#         print(f"[{self.nombre} ha ingresado]. La pizarra global ahora marca: {RegistroVisitantes.total_personas}")

# # nace el priemr objeto, la pizarra sube a 1 
# persona1 = RegistroVisitantes("Diego")

# # nace el segundo objeto. la pizarra sube a 2
# persona2 = RegistroVisitantes("María")

# # nace persona 3, la pizarra sube a 3
# persona3 = RegistroVisitantes("Juan")


# print(f"\nTotal final del dia de personas es: {RegistroVisitantes.total_personas}")




class EmpleadoTienda:

    # atributos de clase
    sueldo_minimo_legal = 300
    cantidad_empleado = 0

    # constructor
    def __init__(self, nombre, id_empleado):
        # nombre 
        self.nombre = nombre
        # id de empleado
        self.id = id_empleado

        # cada vez que nace un empleado, modificamos el atributo de clase
        EmpleadoTienda.cantidad_empleado += 1

    # metodo de clase(la ley modifica el aumento del salario)
    @classmethod
    def aumento_nacional(cls, nuevo_salario):
        # recordatorio, usar cls y no self en los métodos de clase
        cls.sueldo_minimo_legal = nuevo_salario

        print("\n[COMUNICADO OFICIAL] El gobierno ha cambiado el sueldo mínimo")

    #  mostrar recibos de pago 
    def mostrar_recibos(self):
        # el objeto lee la informacion compartida de su clase y sus datos propios
        print(f"Empleado {self.id}: {self.nombre} | Pago a recibir: {EmpleadoTienda.sueldo_minimo_legal}")



# programa principal
# print de encabezado
print("\n -- SISTEMA DE PLANILLA NACIONAL --")

# creamos 2 personas empleadas
trabajador1 = EmpleadoTienda("Juan", 1)
trabajador2 = EmpleadoTienda("Luis", 2)


# comprobar que la variable compartida funcionó (contador)
print(f"Total de empleados: {EmpleadoTienda.cantidad_empleado}")

# día de pago 
# generar los recibos de ambos empleados
trabajador1.mostrar_recibos()
trabajador2.mostrar_recibos()

# el gobierno interviene, aumentamos el sueldo mínimo
EmpleadoTienda.aumento_nacional(400)

# siguiente semana de pago
# generar los recibos de ambos empleados
trabajador1.mostrar_recibos()
trabajador2.mostrar_recibos()




