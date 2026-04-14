class DronVigilancia:
    def __init__(self, nombre, modelo):
        self.nombre = nombre
        self.modelo = modelo
        self.bateria = 100
        self.estado = "En Tierra"   

    def mostrar_estado(self):
        print(f"\n--- ESTADO ACTUAL: {self.nombre} [{self.modelo}] ---")
        print(f"Bateria: {self.bateria}% | Estado: {self.estado}")

    def despegar(self):
        if self.estado == "En Vuelo":
            print("El dron ya está volando.")
            return
        if self.bateria < 25:
            print("No se puede despegar, batería muy baja (necesita minimo 25%)")
            return
        self.estado = "En Vuelo"
        print("Despegue exitoso")

    def patrullar(self):
        if self.estado != "En Vuelo":
            print("Error: el dron debe estar en el aire para patrullar.")
            return
        
        self.bateria = self.bateria - 30
        print("Patrullaje realizado (consumo 30%)")
        
        if self.bateria < 10:
            print(f"Batería critica ({self.bateria}%) Aterrizando por seguridad")
            self.estado = "En Tierra"
            self.bateria = 0
        else:
            print(f"Bateria restante: {self.bateria}%")

    def recargar(self):
        if self.estado != "En Tierra":
            print("No se puede recargar en vuelo. Debe estar en tierra.")
            return
        self.bateria = 100
        print("Recarga completa. Bateria al 100%")

    def salir(self):
        print("Cerrando sistema SkyWatch ")
        return True


# Programa principal
print(">>> INICIANDO SISTEMA SKYWATCH <<<")

nombre = input("Ingrese nombre del dron: ")
modelo = input("Ingrese modelo del dron: ")

drone = DronVigilancia(nombre, modelo)   # uso "drone" en vez de "dron" para variar

while True:
    drone.mostrar_estado()
    
    print("\n¿Que accion desea realizar?")
    print("1. Despegar")
    print("2. Patrullar")
    print("3. Recargar")
    print("4. Salir")
    
    opcion = input("Opción (1-4): ")
    
    if opcion == "1":
        drone.despegar()
    elif opcion == "2":
        drone.patrullar()
    elif opcion == "3":
        drone.recargar()
    elif opcion == "4":
        drone.salir()
        break
    else:
        print("Opcion invalida, intente de nuevo.")