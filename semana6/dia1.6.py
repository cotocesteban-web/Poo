### nuevo tema:
### *** ARQUITECTURA DE SOFTWARE:
# factory (la fabrica)

# # contrato
# from abc import ABC, abstractmethod


# class Personaje(ABC):
#     @abstractmethod
#     def atacar(self):
#         pass

# # modelos concretos
# class Guerrero(Personaje):
#     def atacar(self): return "Ataca con espada"

# class Mago(Personaje):
#     def atacar(self): return "Ataca con magia"

# # la fábrica (el corazón del patrón)
# class FabricaPersonajes:
#     @staticmethod
#     def crear_personaje(tipo):
#         # este método centraliza toda la lógica de creación 
#         tipo = tipo.lower()

#         if tipo == "guerrero":
#             return Guerrero()
#         elif tipo == "mago":
#             return Mago()
#         else:
#             raise ValueError(f"La fábrica no sabe crear: {tipo}")



# try:
#     eleccion = input("Qué personake deseas: (Guerrero / Mago)")

#     # el main NO hace: if eleccion == "guerrero: Guerrero()
#     # el main DELEGA a la fábrica
#     heroe = FabricaPersonajes.crear_personaje(eleccion)
#     print(heroe.atacar())
# except ValueError as error:
#     print(error)


# MODELO (lógica pura)
# class Tarea:
#     def __init__(self, descripcion):
#         self.descripcion = descripcion 
#         self. completada = False


# # VISTA 
# class VistaTarea:
#     @staticmethod
#     def mostrar_menu():
#         print("\n 1. Agregar tarea\n 2. Mostar tarea\n 3. Salir")
#         return input("Opción: ")

#     @staticmethod
#     def mostrar_lista(lista):
#         print("\nLista de tareas: ")

#         for tarea in lista:
#             estado = "Completada" if tarea.completada else "Pendiente"
#             print(f"{tarea.descripcion} está en estado: {estado}")

#     @staticmethod
#     def solicitar_descripcion():
#         return input("Descripción de la tarea: ")
    
#     def mostrar_mensaje(self,mensaje):
#         print(mensaje)

# # CONTROLADOR
# class ControladorTareas:
#     def __init__(self):
#         self.tareas = []
#         self.vista = VistaTarea()

#     def ejecutar(self):
#         while True:
#             opcion = self.vista.mostrar_menu()
#             if opcion == "1":
#                 descripcion = self.vista.solicitar_descripcion()
#                 tarea = Tarea(descripcion)
#                 self.tareas.append(tarea)
#             elif opcion == "2":
#                 self.vista.mostrar_lista(self.tareas)
#             elif opcion == "3":
#                 self.vista.mostrar_mensaje("Saliendo...")
#                 break
    

# # inicio del programa 
# if __name__ == "__main__":
#     controlador = ControladorTareas()
#     controlador.ejecutar()
                


### ejercicio: MCV
## 
### Constructor estes la base del sistema
class Libro:
    def __init__(self, titulo, autor, id):
        self.titulo = titulo
        self.autor = autor
        self.id = id
        self.estado = False  
    def marcar_estado(self):
        self.estado = True

# modelo

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def listar_libros(self):
        return self.libros

    def prestar_libro(self, id):
        for libro in self.libros:
            if libro.id == id:
                if not libro.estado:
                    libro.marcar_estado()
                    return True
                else:
                    return False
        return None


# vista
class VistaBiblioteca:

    @staticmethod
    def mostrar_menu():
        print("\n1. Agregar libro")
        print("2. Listar libros")
        print("3. Prestar libro")
        print("4. Salir")
        return input("Seleccione una opción: ")

    @staticmethod
    def pedir_datos_libro():
        titulo = input("Titulo: ")
        autor = input("Autor: ")
        id = input("ID: ")
        return titulo, autor, id

    @staticmethod
    def pedir_id_libro():
        return input("Ingrese el ID del libro: ")

    @staticmethod
    def mostrar_libros(libros):
        print("\nLista de libros:")
        for libro in libros:
            estado = "Prestado" if libro.estado else "Disponible"
            print(f"{libro.id} | {libro.titulo} | {libro.autor} | {estado}")

    @staticmethod
    def mostrar_mensaje(mensaje):
        print(mensaje)

# Contorlador
class ControladorBiblioteca:
    def __init__(self):
        self.modelo = Biblioteca()

    def ejecutar(self):
        while True:
            opcion = VistaBiblioteca.mostrar_menu()

            if opcion == "1":
                titulo, autor, id = VistaBiblioteca.pedir_datos_libro()
                libro = Libro(titulo, autor, id)
                self.modelo.agregar_libro(libro)
                VistaBiblioteca.mostrar_mensaje("Libro fue agragdo.")

            elif opcion == "2":
                libros = self.modelo.listar_libros()
                VistaBiblioteca.mostrar_libros(libros)

            elif opcion == "3":
                id = VistaBiblioteca.pedir_id_libro()
                resultado = self.modelo.prestar_libro(id)

                if resultado is True:
                    VistaBiblioteca.mostrar_mensaje("Libro prestado")
                elif resultado is False:
                    VistaBiblioteca.mostrar_mensaje("El libro ya esta prestado")
                else:
                    VistaBiblioteca.mostrar_mensaje("Libro no encontrado")

            elif opcion == "4":
                VistaBiblioteca.mostrar_mensaje("Cerrando el programa")
                break

# MAIN
if __name__ == "__main__":
    app = ControladorBiblioteca()
    app.ejecutar()
