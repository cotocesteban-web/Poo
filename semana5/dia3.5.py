### repaso dia 2
# formas de importar Librerias 
# usar alias uasndo "as"
# sobrecarga de operadores
#sobrecarga de metodos 
# reportar herramientas especificas y no toda la libreria: from (nombre de la librerias) import(nombre de la herramienta
# Imporatar nuestras propias librerias

### ejercicio rapid

# 1. Importa la librería random como rd
# import random as rd


# class SableDeLuz:
#     def __init__(self):
#         self.energia = 100

#     def recargar(self, cantidad=None):
#         if cantidad is None:
#             self.energia += 10
#         else:
#             self.energia += cantidad
        

#     def __sub__(self, cantidad):
#         self.energia -= cantidad
#         return cantidad

# def log(sable):
#     print(f"Estado del Sable de Luz: {sable.energia}% de energía.")


# mi_sable = SableDeLuz()

# mi_sable - 30 

# mi_sable.recargar()      
# mi_sable.recargar(5)     

# log(mi_sable)



# #### **concepto Abstracto


# class FiguraGeometrica:
#     def calcular_area(self,):
#         print(" NO dr como calcular el area . No soy una figura")

#     class Cuadrado(FiguraGeometrica):
#         def calcular_area(self,):
#             print(" Area = lado * lado")

# ## * creando el molde fantasma ( el modulo "abc")
# ## "abc" = Abstract Base Clasess
# # debemos marcar al menos uno de sus metodos con el decorador @abstractmethod
# # metodo abstracto es un ketodo vacio. NO tirn codigo por dentro. usamos la pallabrea pass

# from abc import ABC, abstractmethod

# class Documento(ABC):
#     def __init__(self, titulo):
#         self.titulo = titulo
#     @abstractmethod
#     def exportar(self):
#         pass

#     def mostrar_titulo(self):
#         print(f"documento: {self.titulo}")

# class PDF (Documento)
#     def exportar(self):
#         print(f"Exportando documento PDF: {self.titulo}")

# try :
#     doc_invalido = Documento("mi archivo")

# except:
#     print("[Error] No se puede instanciar un documento directamente. Es una clase abstracta.bolqueo de seguridad")

# pdf_doc = PDF("Reporte de Ventas")
# pdf_doc.mostrar_titulo()
# pdf_doc.exportar()

# print("="*10)

# ## El hijo esta obligadoa sobreescribir Todos los metro  del padre


# ## ejercicio:

# from abc import ABC, abstractmethod
# class Trabajador(ABC):
#     def __init__(self, realizar_tarea):
#         self.realizar_tarea = realizar_tarea

#     @abstractmethod
#     def realiza_tarea(self):
#         pass

# class Ingeniero(Trabajador):
#     print("Disenando planos")

# class Medico(Trabajador):
#     def realiza_tarea(self):
#         pass

# inge = Ingeniero()
# inge.realizar_tarea()

# try: 
#     trbajador_invalido

    
# ### Pendiente de terminar con exeept y try
# from abc import ABC, abstractmethod

# 1. La plantilla (Clase Abstracta)
class Trabajador(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def realiza_tarea(self):
        pass

# 2. Clase Ingeniero
class Ingeniero(Trabajador):
    def realiza_tarea(self):
        print(f"{self.nombre} está diseñando planos.")

# 3. Clase Medico (¡Aquí está el que necesitabas!)
class Medico(Trabajador):
    def realiza_tarea(self):
        print(f"{self.nombre} está atendiendo pacientes.")

# --- PRUEBAS ---

# Creamos al ingeniero
inge = Ingeniero("Carlos")
inge.realiza_tarea()

# Creamos al médico
doc = Medico("Dra. Elena")
doc.realiza_tarea()

print("-" * 30)

# Intento inválido (para probar el try/except)
try: 
    print("Intentando crear un trabajador genérico...")
    alguien = Trabajador("Persona X")
except: 
    print("ERROR: No se puede crear un 'Trabajador' directamente.")
    print("Debes usar una profesión específica (Ingeniero o Medico).")




## Propiedads abstractas:
# from abc import ABC, abstractmethod

# class VehiculoComercial(ABC):
#     @property
#     @abstractmethod
#     def tarifa_km(self):
#         pass

#     def calcular_viaje(self, kilometro):
#         total = kilometro * self.tarifa_km
        



## Herencia Multiple hereda de papa y mama
# aca fala el ejemplo:





### Ejercicio integrador:

from abc import ABC, abstractmethod

class VehiculoTerrestre(ABC):
    @abstractmethod
    def conducir_ruedas(self):
        pass

class VehiculoAcuatico(ABC):
    @abstractmethod
    def encender_helices(self):
        pass
class VehiculoAnfibio(VehiculoTerrestre,VehiculoAcuatico):
    def conducir_ruedas(self):
        print("Activando traccion 4x4 en terreno rocoso:")

    def encender_helices(self):
        print("Retrayendo ruedas y activando propulsion acuatica.")

class AutoComun(VehiculoTerrestre):
    def conducir_ruedas(self):
        print("Vehiculo avanzando")

class Lancha(VehiculoAcuatico):
    def encender_helices(self):
        print("Lancha dando marcha.")

try: 
    auto = AutoComun()
    lancha = Lancha()
    anfibio = VehiculoAnfibio()
    ruta = [auto, anfibio]
    for lista in ruta:
        lista.conducir_ruedas()

    ruta_acuatica = [lancha, anfibio]
    for lista in ruta_acuatica:
        lista.encender_helices()

except:
    print("Algo salio mal")






      


