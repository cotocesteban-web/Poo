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

    # Metodo de clase
    @classmethod
    def modificar_tasa_interes(cls, nueva_tasa):
        cls.tasa_interes_global = nueva_tasa
        print(f"\n'COMUNICADO DEL BANCO' La tasa de interés global ha sido actualizada a {nueva_tasa*100}%.")



print("\n -- SISTEMA BANCARIO - SIMULACIÓN --\n")

cuenta1 = CuentaBancaria("Sofia")
cuenta2 = CuentaBancaria("Carlos")


print(f"Total de cuentas creadas en el banco: {CuentaBancaria.total_cuentas_creadas}")


print("\n--- Operaciones con la cuenta de Sofia ---")
cuenta1.depositar(10000)
cuenta1.proyectar_intereses()        

CuentaBancaria.modificar_tasa_interes(0.10)


cuenta1.proyectar_intereses()


print("\n--- Prueba de seguridad del setter ---")
cuenta1.titular = ""  

 
print(f"Titular: {cuenta1.titular} | Saldo: Q{cuenta1.saldo:.2f}")
print(f"Titular: {cuenta2.titular} | Saldo: Q{cuenta2.saldo:.2f}")
print(f"Total de cuentas en el banco: {CuentaBancaria.total_cuentas_creadas}")