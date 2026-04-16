# repao del dia 4:


# nuevo tema
# Composicion basica:
# 

# class Motor:
#     def __init__(self, caballos_fuerza):
#         self.caballos = caballos_fuerza
#         self.encendido = False

#         def arrancar(self):
#             self.encendido = True
#             print("Encendiendo el motor")

# class Auto:
#     def __init__(self, marca, modelo, potencia_motor):
#         self.marca = marca
#         self.modelo = modelo

#         self.corazon_mecanico = Motor(potencia_motor)


#     def encender_auto(self):
#         print("girando llave")
#         self.corazon_mecanico.arrancar()

# mi_carro = Auto()


## pendiente terminar

## ejercicio:

# class Bateria:
#     def __init__(self):
#         self.porcentaje = 100

#     def descargar(self):
#         self.porcentaje -= 10
#         print(f"Bateria al {self.porcentaje}")

# class Celular:
#     def __init__(self, marca):
#         self.marca = marca
#         self.energia = Bateria()
    
#     def usar_app(self):
#         print("Inicializanco app")
#         self.energia.descargar()

# mi_celular = Celular("motorola")
# mi_celular.usar_app()
# mi_celular.usar_app()



#3 inyeccion de piezas(nObjetos como Parametros)
# *** inyeccion de dependencias: **
# Ejemplo:

# class Procesador :
#     def __init__(self, modelo):

##pendiente....


## ejercicio:
class Arma:
    def __init__(self, nombre, puntos_dano):
        self.nombre = nombre
        self.puntos_dano = puntos_dano

class Guerrero:
    def __init__(self, nombre, arma_equipada):
        self.nombre = nombre
        self.arma = arma_equipada

    def atacar(self):
        print(f"El guerrero {self.nombre} Ataca con: {self.arma} causando puntos de dano: {self.puntos_dano}")

# 1. Creamos el arma primero
mi_arma = Arma("Espada larga", 50)

# 2. Creamos al guerrero y le ENTREGAMOS el arma
guerrero1 = Guerrero("Ragnar", mi_arma)

# 3. Mandamos a atacar
guerrero1.atacar()

    
#### Relacione 1 a Muchos (lista de objetos)
class Estudiante:
    def __init__(self, nombre, carnet):
        self.nombre = nombre
        self.carnet = carnet 

class Curso:
    def __init__(self, nombre_curso):
        self.nombre_curso = nombre_curso

        self.lista_matriculados = []

    def matricular(self, nuevo_estudiante):
        self.lista_matriculados.append(nuevo_estudiante)

        print(f"Sistema: {nuevo_estudiante.nombre} matriculado con éxito")

    def pasar_lista(self):
        for alumno in self.lista_matriculados:
            print(f"{alumno.carnet}: {alumno.nombre}")

alumno1 = Estudiante("Luis", "A001")
alumno2 = Estudiante("Keyla", "A002")

curso_poo = Curso("POO")

curso_poo.matricular(alumno1)
curso_poo.matricular(alumno2)

curso_poo.pasar_lista()

curso_poo.lista_matriculados[0].nombre = "Luis Fernando"

curso_poo.pasar_lista()



### ejercicio Integrador
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def __str__(self):
        return f'"{self.titulo}" escrito por {self.autor}'


class Biblioteca:
    def __init__(self, nombre_sucursal):
        self.nombre_sucursal = nombre_sucursal
        self.catalogo = []          # Lista vacía para almacenar los libros
    
    def agregar_libro(self, nuevo_libro):
        self.catalogo.append(nuevo_libro)
    
    def mostrar_inventario(self):
        print(self.nombre_sucursal)
        for libro in self.catalogo:
            print(libro)   



libro1 = Libro("Cien años de soledad", "Gabriel García Márquez")
libro2 = Libro("El principito", "Antoine de Saint-Exupéry")
libro3 = Libro("1984", "George Orwell")


biblioteca = Biblioteca("Biblioteca Central")

# 3. Agregar los libros al catálogo
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

# 4. Mostrar el inventario
biblioteca.mostrar_inventario()

