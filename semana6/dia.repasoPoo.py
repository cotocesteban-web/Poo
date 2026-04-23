import json
from abc import ABC, abstractmethod

# ==========================================
# A. EL MODELO (modelo.py integrado)
# ==========================================
class FuenteEnergia(ABC):
    def __init__(self, id_generador, capacidad_maxima):
        self.id_generador = id_generador
        self.capacidad_maxima = capacidad_maxima
        self.produccion_actual = 0.0

    @abstractmethod
    def generar(self, datos_clima):
        pass

class PanelSolar(FuenteEnergia):
    def generar(self, datos_clima):
        # Solo genera energía si el clima es "Soleado"
        if datos_clima.get("clima") == "Soleado":
            self.produccion_actual = self.capacidad_maxima
        else:
            self.produccion_actual = 0.0
        return self.produccion_actual

class TurbinaEolica(FuenteEnergia):
    def generar(self, datos_clima):
        viento = datos_clima.get("viento", 0)
        
        # Validación de viento (corregida la identación)
        if viento <= 0:
            self.produccion_actual = 0.0
            return self.produccion_actual

        # Calculamos y limitamos a la capacidad máxima
        calculo = viento * 5.0
        if calculo > self.capacidad_maxima:
            self.produccion_actual = self.capacidad_maxima
        else:
            self.produccion_actual = calculo
            
        return self.produccion_actual

class GeneradorDiesel(FuenteEnergia):
    def __init__(self, id_generador, capacidad_maxima, combustible):
        super().__init__(id_generador, capacidad_maxima)
        self.combustible = combustible

    def generar(self, datos_clima):
        # Consume combustible si hay disponible (10L por ciclo)
        if self.combustible >= 10:
            self.produccion_actual = self.capacidad_maxima
            self.combustible -= 10
        else:
            self.produccion_actual = 0.0
        return self.produccion_actual

# ==========================================
# B. LA FÁBRICA (fabrica.py integrada)
# ==========================================
class FabricaEnergia:
    _mapeo = {
        "solar": PanelSolar,
        "eolica": TurbinaEolica,
        "diesel": GeneradorDiesel
    }

    @staticmethod
    def crear_fuente(datos):
        # Corregida la identación del método estático y el match
        tipo = datos.get("tipo")
        match tipo:
            case "solar":
                return PanelSolar(datos["id_generador"], datos["capacidad_maxima"])
            
            case "eolica":
                return TurbinaEolica(datos["id_generador"], datos["capacidad_maxima"])
            
            case "diesel":
                return GeneradorDiesel(
                    datos["id_generador"], 
                    datos["capacidad_maxima"], 
                    datos.get("combustible", 100)
                )
            case _:
                return None

# ==========================================
# C. LA VISTA (vista.py integrada)
# ==========================================
class InterfazRed:
    @staticmethod
    def mostrar_tablero(fuentes):
        print("\n" + "="*55)
        print("          ESTADO DE LA CIUDAD INTELIGENTE")
        print("="*55)
        print(f"{'ID':<10} | {'TIPO':<15} | {'PRODUCCIÓN':<15}")
        print("-" * 55)
        for f in fuentes:
            tipo = f.__class__.__name__
            print(f"{f.id_generador:<10} | {tipo:<15} | {f.produccion_actual:>8.2f} kW")
        print("="*55 + "\n")

    @staticmethod
    def solicitar_datos_entorno():
        print("\n>>> CONFIGURACIÓN DEL ENTORNO")
        try:
            clima = input("Estado del clima (Soleado/Nublado): ").strip().capitalize()
            viento = float(input("Velocidad del viento (km/h): "))
            return {"clima": clima, "viento": viento}
        except ValueError:
            print("[!] Entrada inválida. Usando valores por defecto.")
            return {"clima": "Nublado", "viento": 0.0}

    @staticmethod
    def mostrar_error(mensaje):
        print(f"\n[SISTEMA]: Error detectado -> {mensaje}\n")

# ==========================================
# D. EL CONTROLADOR (controlador.py integrado)
# ==========================================
class ControladorRed:
    def __init__(self, json_data):
        self.fuentes = []
        self.vista = InterfazRed()
        self.json_data = json_data

    def inicializar_red(self):
        try:
            config = json.loads(self.json_data)
            for item in config:
                fuente = FabricaEnergia.crear_fuente(item)
                if fuente:
                    self.fuentes.append(fuente)
        except Exception as e:
            self.vista.mostrar_error(f"Fallo en carga: {e}")

    def ejecutar(self):
        self.inicializar_red()
        
        if not self.fuentes:
            self.vista.mostrar_error("Red vacía o configuración inválida.")
            return

        # Ciclo de simulación
        datos_entorno = self.vista.solicitar_datos_entorno()
        
        for fuente in self.fuentes:
            fuente.generar(datos_entorno)
            
        self.vista.mostrar_tablero(self.fuentes)

# ==========================================
# PUNTO DE ARRANQUE
# ==========================================
if __name__ == "__main__":
    contenido_json = """
    [
        {"tipo": "solar", "id_generador": "SOL-01", "capacidad_maxima": 100.0},
        {"tipo": "eolica", "id_generador": "EOL-99", "capacidad_maxima": 250.0},
        {"tipo": "diesel", "id_generador": "DSL-05", "capacidad_maxima": 500.0, "combustible": 1000.0}
    ]
    """
    
    app = ControladorRed(contenido_json)
    app.ejecutar()