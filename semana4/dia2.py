#### encapsulamineto ###

### nuevo tema##
# colocarle un candado ala informacion con ventanila de informacion getter y selller:
# sintaxis : Para convertir un atributo publico en *privado* invisible para el munco exterior  simplemente colocamos dos guiones bajos al inicio
# de sunombre del constructor. (__)
# class Cuenta:
#     def __init__(self, saldo_inicial):
#         self.nombre = "publica"
#         self.__saldo = saldo_inicial


# mi_cuenta = cuenta(1000)
# print(mi_cuenta.nombre)
# print(mi_cuenta__saldo) ## error phyton no permite acceder a atributos privados desde afuera de la calase


### 2do ejemplo

# class UsuarioBancario:
#     def __init__(self, nombre_ingresado, pin_ingresado):
#         self.nombre = nombre_ingresado
#         ### atributo privado
#         self.__pin = pin_ingresado
#     ### gett tradicional opara consultar
#     def get_pin(self):
#         return self.__pin
#     ## set_pin
#     def set_pin(self, nuevo_pin):
#         # validacion
#         if len(str(nuevo_pin)) == 4:
#             self.pin = nuevo_pin
#             print("operacion exitosa")
#         else:
#             print("error")

# cliente = UsuarioBancario("Diego", 1234)
# ## intentar acceder directamente al aributo privado
# pin_cliente = cliente.get_pin()
# print(cliente.get_pin)
# cliente.set_pin(5544)
# print(cliente.get_pin)
# pin_cliente = cliente.get_pin()
# cliente.set_pin (4444)
# pin_cliente = cliente.get_pin()
# print(pin_cliente)   


## Ejercicio:
### Creamos la clase y la construimos con __init__ los atributos:
class RegistroAcademico:
    def __init__(self, nombre_alumno, nota_inicial):
        ## Definimos atributo publico
        self.nombre = nombre_alumno
        ## Atributo privado
        self.__nota = nota_inicial
        ## Estado de cuenta publico por defecto
        self.cuenta_activa = True
## Metodo o funcion de retornar nota es Privado
    def get_nota(self):
        return self.__nota
## Metodo o funcion de Bloquear cuenta
    def  bloquear_cuenta(self):
        self.cuenta_activa = False
## Metodo o Funcion de la nueva nota
    def set_nota(self, nueva_nota):
        ## Comparacion si la cuenta esta activa para proceder:
        if self.cuenta_activa == False:
            return -2
## comparacion si la nota esta en el rango de 0 a 100
        elif 0 <= nueva_nota <= 100:
            return 1
        else:
            return -1
    
alumna = RegistroAcademico("Laura", 85)
intentos = 3
while intentos >  0 :
    nueva_nota = int(input("Ingrese la nueva nota: "))
    resultado_ingreso = alumna.set_nota(nueva_nota)
    if resultado_ingreso == 1:
        print(f"Felicidades la nota ha sido actualizada: {nueva_nota}")
        break
    elif resultado_ingreso == - 1:
        intentos = intentos - 1
        print(f"Intentos restantes: {intentos}")

if intentos == 0:
    alumna.bloquear_cuenta()
    print(f"Llego Limite de intentos: {intentos} su cuenta se a bloqueado")










