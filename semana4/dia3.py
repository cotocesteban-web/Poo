## estilo profesional de python (@ property)
## ejemplo en phyton
# class Temperatura:
#     def __init__(self):
#         self.__grados = 20

#     @property
#     def grados(self):
#      return self.___grados
        
# clima = Temperatura()



## ejercicio:

# class Empleado:
#     def __init__(self):
#       self.__salario = 300
#     @property
#     def salario (self):
#         return self.__salario

#     @salario.setter
#     def salario(self, nuevo_salario):
#         if nuevo_salario <= 300:
#           print(f"Salario invalido es mayor es menor a 300 {nuevo_salario}")
#         else:
#           print(f"El cambio de salario se realizo: {nuevo_salario}")

# salario_empleado = Empleado()
# print(salario_empleado.salario)
# salario_empleado.salario = 400

# ## Ejercicio 2  
# class Climatizacion:
#     def __init__(self):
#       self.__temperatura = 20
#     @property
#     def temperatura (self):
#         return self.__temperatura
    
#     @temperatura.setter
#     def temperatura (self, nueva_temperatura):
#        while nueva_temperatura >= 20 or nueva_temperatura <= 16:
#           print(F"Ajuste de temperatura no valido: {nueva_temperatura}")
#           nueva_temperatura = int(input("ingrese la temperatura deseada"))
#           self.temperatura = nueva_temperatura
#           print(f"Temperatura ajustado correctamente{nueva_temperatura}")

# ajuste_temperatura = Climatizacion()
# print()


### Atributos y metodos de clase

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
#

## ejercicio integrador:


class CuentaBancaria:
    tasa_interes_global = 0.05
    total_cuentas_craeadas = 0
    
    def __init__(self, nombe_titular):
        self.titular = nombe_titular
        self.__saldo = 0.0
        






        

