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

    # losatibutos de clase 
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

    # Atributos de clase (compartidos por todas las cuentas)
    tasa_interes_global = 0.05
    total_cuentas_creadas = 0

    # Constructor
    def __init__(self, nombre_titular):
        # estos son los atributos privados
        self.__titular = nombre_titular
        self.__saldo = 0.0

        # Cada vez que se crea una cuenta, aumentamos el contador global
        CuentaBancaria.total_cuentas_creadas += 1

    # Property para saldo (solo Getter - no se permite setter directo)
    @property
    def saldo(self):
        return self.__saldo

    # Property para titular con Getter y Setter seguro
    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, nuevo_nombre):
        if nuevo_nombre.strip() == "":   # valida que no esté en blanco
            print("Error: El nombre del titular no puede estar en blanco.")
        else:
            self.__titular = nuevo_nombre

    # Metodos de instancia
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Deposito exitoso de Q{cantidad} su saldo actual es: {self.__saldo}")
        else:
            print("Error: La cantidad a depositar debe ser mayor a 0")

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Retiro exitoso de Q{cantidad} Saldo actual: Q{self.__saldo}")
        elif cantidad > self.__saldo:
            print("Su saldo es insuficiente es menor al retiro.")

    def proyectar_intereses(self):
        interes = self.__saldo * CuentaBancaria.tasa_interes_global
        self.__saldo += interes
        print(f"Intereses ganados Q{interes:.2f}")
        print(f"Nuevo Q{self.__saldo:.2f}")

    # Método de clase
    @classmethod
    def modificar_tasa_interes(cls, nueva_tasa):
        cls.tasa_interes_global = nueva_tasa
        print(f"\n[COMUNICADO DEL BANCO] La tasa de interés global ha sido actualizada a {nueva_tasa*100}%.")



print("\n -- SISTEMA BANCARIO - SIMULACIÓN --\n")

cuenta1 = CuentaBancaria("Sofia")
cuenta2 = CuentaBancaria("Carlos")

# Mostrar total de cuentas creadas
print(f"Total de cuentas creadas en el banco: {CuentaBancaria.total_cuentas_creadas}")

# O
print("\n--- Operaciones con la cuenta de Sofia ---")
cuenta1.depositar(10000)
cuenta1.proyectar_intereses()          # con tasa del 5%

# El banco sube la tasa de interés al 10%
CuentaBancaria.modificar_tasa_interes(0.10)

# Proyectar intereses nuevamente con la nueva tasa
cuenta1.proyectar_intereses()

# Intentar cambiar el nombre a vacío (debe bloquearse)
print("\n--- Prueba de seguridad del setter ---")
cuenta1.titular = ""   # debe mostrar error

# Mostrar información final
print("\n--- Estado final de las cuentas ---")
print(f"Titular: {cuenta1.titular} | Saldo: Q{cuenta1.saldo:.2f}")
print(f"Titular: {cuenta2.titular} | Saldo: Q{cuenta2.saldo:.2f}")
print(f"Total de cuentas en el banco: {CuentaBancaria.total_cuentas_creadas}")





        

