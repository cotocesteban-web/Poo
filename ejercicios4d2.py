class Caja_registradora():
    def cobrar_producto(self):
        precio = float(input("Ingrese el presio del producto: "))
        self.dinero_acumulado = precio + self.dinero_acumulado
        print (f"Cobro exitoso. llevamos acumulado Q:{self.dinero_acumulado}.")

    def imprimir_cierre_turno (self):
        print(f"Cajero: {self.cajero_asignado},total Q:{self.dinero_acumulado} al cierre.")
        


caja_express = Caja_registradora()
caja_express.cajero_asignado = "Carlos"
caja_express.dinero_acumulado = 0


caja_express.cobrar_producto()
caja_express.cobrar_producto()
caja_express.imprimir_cierre_turno()