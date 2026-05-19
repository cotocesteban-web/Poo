from abc import ABC, abstractmethod

class NucleoEnergia:
    def __init__(self, nivel_inicial=100):
        self.nivel = nivel_inicial

    def consumir(self, cantidad):
        if self.nivel - cantidad < 0:
            raise ValueError("Energía insuficiente.")
        self.nivel -= cantidad

class NaveEspacial(ABC):
    _total_naves_fabricadas = 0

    def __init__(self, nombre, registro):
        self.nombre = nombre
        self.registro = registro
        self.__combustible = 100
        self.__escudos = 100
        self.estado = "Operativo"
        self.nucleo = NucleoEnergia()
        NaveEspacial._total_naves_fabricadas += 1

    @property
    def escudos(self):
        return self.__escudos

    @escudos.setter
    def escudos(self, valor):
        self.__escudos = max(0, min(valor, 100))
        if self.__escudos == 0:
            self.estado = "Vulnerable"

    @abstractmethod
    def mision_especializada(self):
        pass

    def __lt__(self, otra):
        # Implementación del operador _lt_ para comparar energía [cite: 28]
        return self.nucleo.nivel < otra.nucleo.nivel

    def __str__(self):
        # Formato de salida para la opción 5 (Stat) 
        return f"Nave: {self.nombre} | Código: {self.registro} | Energía: {self.nucleo.nivel}% | Escudo: {self.escudos}%"

class NaveCombate(NaveEspacial):
    def __init__(self, nombre, registro, potencia_fuego):
        super().__init__(nombre, registro)
        self.potencia_fuego = potencia_fuego

    def mision_especializada(self):
        # Salida esperada según el flujo [cite: 48]
        return f"Desplegando ataque con potencia {self.potencia_fuego}."

class NaveCarga(NaveEspacial):
    def __init__(self, nombre, registro, capacidad):
        super().__init__(nombre, registro)
        self.capacidad = capacidad

    def mision_especializada(self):
        return f"Transportando {self.capacidad} toneladas."

class InterceptorHibrido(NaveCombate, NaveCarga):
    def __init__(self, nombre, registro, potencia, capacidad):
        NaveCombate.__init__(self, nombre, registro, potencia)
        self.capacidad = capacidad

    def mision_especializada(self):
        return f"Misión de Élite: Ataque y transporte ({self.capacidad}T)."

class EstacionEspacial:
    def __init__(self):
        self.hangar = []

    def inyectar_nave(self, nave):
        self.hangar.append(nave)

# --- PROGRAMA PRINCIPAL ---

def ejecutar_sistema():
    estacion = EstacionEspacial()
    print(">>> ESTACIÓN AETHELGARD ACTIVADA <<<") 
    
    while True:
        print("\n1. Registrar | 2. Misión | 3. Comparar | 4. Fusionar | 5. Stat | 6. Salir") 
        try:
            opcion = input("Seleccione acción: ") 

            if opcion == "1":
                tipo = input("Tipo (1. Combate, 2. Carga, 3. Híbrida): ") 
                nom = input("Nombre: ") 
                reg = input("Código: ")
                
                if tipo == "1":
                    pwr = int(input("Potencia: ")) 
                    estacion.inyectar_nave(NaveCombate(nom, reg, pwr))
                elif tipo == "2":
                    cap = int(input("Capacidad: ")) 
                    estacion.inyectar_nave(NaveCarga(nom, reg, cap))
                
                print(f"Éxito. Total naves fabricadas: {NaveEspacial._total_naves_fabricadas}") 

            elif opcion == "2":
                idx = int(input("Índice de nave: ")) 
                costo = int(input("Energía a consumir: ")) 
                nave = estacion.hangar[idx]
                nave.nucleo.consumir(costo)
                print(f"Resultado: {nave.mision_especializada()}") 

            elif opcion == "3":
                idx1 = int(input("Índice nave 1: ")) 
                idx2 = int(input("Índice nave 2: ")) 
                if estacion.hangar[idx1] < estacion.hangar[idx2]:
                    print(f"{estacion.hangar[idx1].nombre} tiene menos energía.") 
                else:
                    print(f"{estacion.hangar[idx1].nombre} tiene más o igual energía.")

            elif opcion == "5":
                for i, nave in enumerate(estacion.hangar):
                    print(f"[{i}] {nave}") [cite: 59]

            elif opcion == "6":
                break

        except ValueError as e:
            # Captura de "error_de_texto" 
            print(f"[ADVERTENCIA] Entrada inválida: {e}")
        except Exception as e:
            print(f"[ERROR] {e}")

if __name__ == "__main__":
    ejecutar_sistema()