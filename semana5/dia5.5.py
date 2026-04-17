### dia 5 Poo
### Ejercicio integrador
from abc import ABC, abstractmethod


class PersonalMedico(ABC):
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad

    @abstractmethod
    def realizar_labor(self):
        pass

class Doctor(PersonalMedico):
    def realizar_labor(self):
        print(f"El Doctor. {self.nombre} esta realizando un diagnóstico especializado.")

    def atender_paciente(self, paciente):
        self.realizar_labor()
        nota = input("Ingrese el diagnostico del paciente: ")
        paciente.historial.agregar_observacion(nota)

        while True:
            try:
                salud = int(input("Ingrese la salud del paciente 0-100: "))
                if 0 <= salud <= 100:
                    paciente.salud = salud
                    break
                else:
                    print("Ingrese un valor entre 0 y 100")
            except:
                print("Solo numeros por favor")

        print(f"La salud del paciente se ha ingresado exitosamente: {paciente.salud}")


class Enfermero(PersonalMedico):
    def realizar_labor(self):
        print(f"El {self.nombre} esta aplicando cuidados y revisando signos vitales.")


class HistorialClinico:
    def __init__(self):
        self.observaciones = []

    def agregar_observacion(self, texto):
        self.observaciones.append(texto)

    def mostrar_historial(self):
        print("Historial de la clnica:")
        for observacion in self.observaciones:
            print(observacion)

class Paciente:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.salud = 0  
        self.historial = HistorialClinico()

    def estado(self):
        if self.salud < 20:
            return "Critico"
        else:
            return "Estable"
        
        ### Sistema central
class Hospital:
    def __init__(self):
        self.pacientes = []
        self.personal = []

    def registrar_paciente(self):
        nombre = input("Ingrese nombre del paciente: ")
        
        while True:
            try:
                edad = int(input("Ingrese edad: "))
                break
            except:
                print("Porfavor ingrese la edad en numeros")

        paciente = Paciente(nombre, edad)
        self.pacientes.append(paciente)
        print("Paciente registrado con exito.")

     ## funcion para contratar personal del hosspital
    def contratar_personal(self):
        nombre = input("Ingrese nombre: ")
        profesion = input("profesion (doctor/enfermero): ").lower()

        if profesion == "doctor":
            especialidad = input("Especialidad: ")
            self.personal.append(Doctor(nombre, especialidad))
        elif profesion == "enfermero":
            self.personal.append(Enfermero(nombre, "Cuidados"))
        else:
            print("Profesion no valido")

    def mostrar_pacientes(self):
        if not self.pacientes:
            print("No hay pacientes registrados")
            return

        for i in range(len(self.pacientes)):
            paciente = self.pacientes[i]
            print(f"{i}. {paciente.nombre} | Edad: {paciente.edad} | Salud: {paciente.salud} | Estado: {paciente.estado()}")
        
    ## Metodo consultas medicas:
    def consulta_medica(self):
        if len(self.personal) == 0 or len(self.pacientes) == 0:
            print("No hay personal o pacientes disponibles")
            return

        for i in range(len(self.personal)):
            trabajador = self.personal[i]
            print(f"{i}. {trabajador.nombre}. {trabajador.especialidad}")


        try:
            medico_seleccion = int(input("Seleccione medico: "))
            medico = self.personal[medico_seleccion]
        except:
            print("Selección inválida\n")
            return

       ### pacientes consulta medica
        for i in range(len(self.pacientes)):
            paciente = self.pacientes[i]
            print(f"{i}, {paciente.nombre}")

        try:
            ingreso_paciente = int(input("Seleccione paciente: "))
            paciente = self.pacientes[ingreso_paciente]
        except:
            print("Selección inválida\n")
            return

        if isinstance(medico, Doctor):
            medico.atender_paciente(paciente)
        else:
            medico.realizar_labor()

hospital = Hospital()

while True:
    print("------ SISTEMA HOSPITALARIO VIDA-SANA ----")
    print("1. Registrar Paciente")
    print("2. Contratar Personal")
    print("3. Consulta Médica")
    print("4. Ver Pacientes")
    print("5. Salir")

    try:
        opcion = int(input("Seleccione una opción: "))
    except:
        print("Ingrese un número válido\n")
        continue

    if opcion == 1:
        hospital.registrar_paciente()
    elif opcion == 2:
        hospital.contratar_personal()
    elif opcion == 3:
        hospital.consulta_medica()
    elif opcion == 4:
        hospital.mostrar_pacientes()
    elif opcion == 5:
        print("Saliendo del sistema...")
        break
    else:
        print("Opción inválida")
    
    




    



