class Empleado ():
    pass

empleado1 = Empleado()
empleado2 = Empleado()
empleado3 = Empleado()

empleado1.nombre = "Daniel"
empleado1.cargo = "Gerente"
empleado1.salario = 15000.0

empleado2.nombre = "Carlos"
empleado2.cargo = "Cajero"
empleado2.salario = 5000.0

empleado3.nombre = "Cristian"
empleado3.cargo = "Bodegero"
empleado3.salario = 5000.0

print(f"Empleado 1: {empleado1.nombre}, Cargo: {empleado1.cargo}, Salario : {empleado1.salario}")
print(f"Empleado 2: {empleado2.nombre}, Cargo: {empleado2.cargo}, Salario : {empleado2.salario}")
print(f"Empleado 3: {empleado3.nombre}, Cargo: {empleado3.cargo}, Salario : {empleado3.salario}")

class Caja_registradora():
    def mostrar_dinero(self):
        print (f"El dinero actual Q: {self.efectivo} ")

    def venta(self):
        dinero_venta = 500
        self.efectivo = dinero_venta + self.efectivo
        print("Procesando una venta nueva.")
        #print(f"total acumulado Q: {self.efectivo}")

caja_r = Caja_registradora ()
caja_r. efectivo = 1000

caja_r.mostrar_dinero()
caja_r.venta()
caja_r.mostrar_dinero()

class TarjetaVIP():
    def mostrar_puntos (self):
        print(f"sus puntos acumulados son: {self.puntos}")

    def suma_puntos(self):
        acumulados = 50
        self.puntos = acumulados + self.puntos
        print("Se han sumado 50 puntos por su compra.")

tarjeta_carlos = TarjetaVIP()

tarjeta_carlos.puntos = 100

tarjeta_carlos.mostrar_puntos()
tarjeta_carlos.suma_puntos()
tarjeta_carlos.mostrar_puntos()
