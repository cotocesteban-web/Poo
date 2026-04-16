### HErencia 

# Principio DRY: DO NOT REPEAT YOURSELF | NO TE REPITAS

# mismo ejemplo de herencia
# class perro:
#     def __init__(self, nombre):
#         self.nombre = nombre
#     def comer(self):

#         print(f"{self.nombre} esta comiendo")

# ## solucion craando herencia
# class animal:
#    pass

# mi_mascota = perro("Firulais")
# mi_mascota.comer() # error porque no se le dio un nombre a mi mascota

## agragando habilidades exclusivas al hijo
# class Vehiculo:
#     def encender_motor(self):
#         print("El motor esta encendido")

#     def apagar_motor(self):
#         print("El motor esta apagado")

# # Subclase 1
# class auto(Vehiculo):
#     def encender_aire(self):
#         print("El aire acondicionado esta encendido")

# # Subclase 2 
# class moto(Vehiculo):
#     def hacer_acrobacia(self):
#         print("La moto esta haciendo una acrobacia")

# ##  Hacer nuestras funciones
# carro =  auto()
# moto1 = moto()
# carro.encender_motor()
# carro.encender_aire()

# # Acciones de la moto 
# print("Acciones de la moto")
# moto1.encender_motor()
# moto1.hacer_acrobacia()

## ejercicio practico: heroes con habilidades unicas
# class PersonajeBase:
#     def caminar(self):
#         print("El personaje esta avanzando por el mapa")
#     def descansar(self):
#         print("El personaje esta recuperando energia")
    

# class Mago(PersonajeBase):
#     def lanzar_hechizo(self):
#         print("!El mago lanza una bola de fuego!")

# class Guerrero(PersonajeBase):
#     def bloquear_ataque(self):
#         print("!El guerrero levanta su escudo de metal!")


# mi_mago = Mago()
# mi_guerrero = Guerrero()
# mi_mago.caminar()
# mi_mago.descansar()

# # Guerrero
# mi_guerrero.caminar()
# mi_guerrero.descansar()

# mi_mago.lanzar_hechizo()
# mi_guerrero.bloquear_ataque()



# ## Constructor del hijo:
# ## ejmoplo:
# class Padre:
#     def __init__(self, apellido):
#         self.nombreapellido = apellido

# class hijo(Padre):
#     def __init__(self, nombre):
#         self.nombre = nombre

# chico = hijo("carlos")
# ## errorel hijo no recibio el apellido

# class persona:
#     def __init__(self, nombre):
#         self.nombre = nombre
#   # el padre hace su trabajp, inicializa el nombre
# class Estudiante(persona):
#     def __init__(self, nombre_ingresado, nota_ingresada):
#         super().__init__(nombre_ingresado) # el super hace que se ejecute el constructor del padre
#         self.nota = nota_ingresada
        
#     def mostrar_info(self):
#         print(f"El estudiante {self.nombre} y mi nota es {self.nota}")

# estudiante1 = Estudiante("Ana", 9.5)
# estudiante1.mostrar_info()


## ejercicio:
# class AlquilerVehiculo:
#     def __init__(self, registrar_autos, disponible, kilometraje, tarifa):
#         self.registrar_autos = registrar_autos
#         self.disponible = disponible
#         self.__kilometraje = kilometraje
#         self.tarifa = tarifa

#     def registrar_auto(self, auto):
#         self.registrar_autos = auto
    
#     def disponible(self, estado):
#         self.disponible = estado

#     def kilometraje(self, kilometros):
#         self.kilometraje += kilometros

#     def tarifa(self, tarifa):
#         self.tarifa = tarifa   
#     @property
#     def kilometraje(self):
#         return self.__kilometraje
#     @kilometraje.setter
#     def kilometraje(self, kilometros):
#         self.__kilometraje += kilometros

# class Alquiler(AlquilerVehiculo):
#     def __init__(self, registrar_autos, disponible, kilometraje, tarifa, cliente):
#         super().__init__(registrar_autos, disponible, kilometraje, tarifa)
#         self.cliente = cliente

#     def mostrar_info(self):
#         print(f"El cliente {self.cliente} alquilo un auto con tarifa de {self.tarifa} y el kilometraje es de {self.__kilometraje}")

# registro = AlquilerVehiculo("Auto1", True, 0, 100)
# registro.registrar_auto("Auto2")
# registro.disponible(False)
# registro.kilometraje(150)
# registro.tarifa(120)

        



### Las muchas formas (Poliformismo)

#  **solid** 
# **S - single responsibility principle (principio de responsabilidad unica)
# **O - open/closed principle (principio de abierto/cerrado)**
# **L - Liskov substitution principle (principio de sustitucion de Liskov)**
# **I - interface segregation principle (principio de segregacion de interfaces)**
# **D - Dependency inversion principle (principio de inversion de dependencias)**

# # ejemplo

# class Empleado:
#     def trabajar(self, nombre, salario):
#         print("El empleado esta trabajando")
#         self.nombtre


# ## La rebelio del hijp (sobreescrituta de metodos)
# class PersonaMayor():
#     def saludar(self):
#         print("La persona mayor saluda con una sonrisa")

# class Adolecente(PersonaMayor):
#     def caminar(self):
#         print("El adolecente camina rapidamente")

# senior = PersonaMayor()
# chico = Adolecente()

# senior.saludar()
# chico.saludar() # 

###Polimorfismo
# class Animal:
#     def __init__(self, nombre):
#         self.nombre = nombre

#     def __str__(self):
#         return f"Soy un animal y mi nombre es {self.nombre}"

#     def hacer_sonido(self.nombre):
#         print(F"{self.nombre} hace un sonido generico")

# class Perro(Animal):
#     def hacer_sonido(self):
#         print(f"{self.nombre} ladra")

# class Gato(Animal):
#     def hacer_sonido(self):
#         print(f"{self.nombre} miau")

# class Pato(Animal):
#     def hacer_sonido(self):
#         print(f"{self.nombre} cuac")

# animal1 = Perro("pochiberto")
# animal2 = Gato("Porfirio")
# animal3 = Pato("Patricio")
# lista_granja = [animal1, animal2]
# lista_granja.append(animal3)

# animal_desconocido = Animal("extraterrrestre")
# lista_granja.append(animal_desconocido)

# print(animal_desconocido)




##conbinando loviejo con lo nuevo:
## Usar super() en metodos normales
class Empleado_base():
    def iniciar_rutina(self):
        print("El empleado esta iniciando su rutina diaria")

class Ejecutivo_Nuevo(Empleado_base):
    def iniciar_rutina(self):
        super().iniciar_rutina() # llama al metodo del padre
        print("El programador esta encendiendo su computadora y revisando su codigo")



trabajador1 = Ejecutivo_Nuevo()
trabajador1.iniciar_rutina()



### Polimorfismo vs Herencia
# ** EJEMPLO 1 hERENCIA SIN PLIMORFISMO


