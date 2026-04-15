# repaso
# ' herencia
# polimorfismo
# super se usa mas con el polimorfismo  cuando quirro agregar alguna instruccion ,e permite modificar lo que el padre hereda
# principio de SOLID
# Sobreescritura de metodos
# __str__

## *** Sobrecarga d eOperadores ***

5+5, 10(matematica)
Hola + mundo, "Hola mundo"(string)


billetera1 + billetera2,
Para enseñar el operador "+" sobreescribimos " __add__(self, otro objeto) (sumar)
para enseñar el operador "-" sobreescribimos " __sub__(self, otro objeto) (restar)
Para enseñar el operador ">" sobreescribimos " __gt__(self, otro objeto) (greater tahn )
para enseñar el operador "<" sobreescribimos " __lt__(self, otro objeto) (less than)
Para enseñar el operador "==" sobreescribimos " __eq__(self, otro objeto) (equal)

#**Ejercicio:**
class Billetera:
    def __init__(self, Propietario, monto):
        self.Propietario = Propietario
        self.monto = monto
    def __add__(self, otra_billetera):
        suma_total = self.monto + otra_billetera.monto

        nuevo_propietario = f" Fondo en conjunto de {self.Propietario} y {otra_billetera.Propietario}"
        return Billetera(nuevo_propietario, suma_total)
    def __gt__(self, otra_billetera):
        return self.monto > otra_billetera.monto

billetera1 = Billetera("Luis", 1000)
billetera2 = Billetera("Juan", 2500)
billetera3 = billetera1 + billetera2
if billetera1 > billetera2:
    print("La billetera 1 tiene mas dinero que la billetera 2")
else:    
    print("La billetera 2 tiene mas dinero que la billetera 1")
billetera_familiar = billetera1 + billetera2
print(f"la billetera creada es {billetera_familiar.Propietario} y el monto total es {billetera_familiar.monto}")
    

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __add__(self, otro_producto):
        return self.precio + otro_producto.precio
    
    def __sub__(self, otro_producto):
        return self.precio - otro_producto.precio
    def __gt__(self, otro_producto):
        return self.precio > otro_producto.precio
    def __str__(self): 
        return f"El producto {self.nombre} tiene un precio de {self.precio}"
    
producto1 = Producto("Camisa", 50)
producto2 = Producto("Pantalon", 80)   
producto3 = Producto("Zapatos", 120)
producto4 = Producto("Gorra", 30)

productos= [producto1, producto2, producto3, producto4]
inventario_total = producto1.precio + producto2.precio + producto3.precio + producto4.precio

producto_caro = producto1 
for producto in productos:
    if producto > producto_caro:
        producto_caro = producto

    
### pendiente
 # 130

## *** Formas de importar librerias:
### ** Forma 1 La bodega de Herramientas (importando modulos) ***
## importando cajas
# vamos a udar la parabra reservada "import" para importar el modulo "caja" que contiene la clase "Caja"
# 
import math
raiz = math.sqrt(16)
print (f"La raiz cuadrada de 16 es {raiz}")


### * forma 2 Importar herramientas especificas de la caja

#3 usamos la sintaxis "from" para importar la clase "Caja" del modulo "caja"
# al hace eso queda la herrramineta suelta de la caja

from math import pi, pow

area_circulo = pi * pow(5, 2)
print(f"El area del circulo es {area_circulo}")

## *Foem 3 Importar con un apodo (Alias)
# pythos nos permite usando la palabra as (como)

import datetime as dt
fecha_hoy = dt.date.today()
print(f"La fecha de hoy es {fecha_hoy}")
 
##* Forma 4 Importar nuectras propias herramientas (modulos creados por nosotros)
## modulos.py solo lamacena no ejecuta 

# -- archivo : modelos.py
## en un archivo llamado modelos.py vamos a crear una clase llamada CalculadoraAvanzada con un metodo sumar_doble que reciba dos numeros y devuelva el resultado de la suma de esos numeros multiplicado por 2, ademas de un metodo saludar que imprima un mensaje de bienvenida.
# en elotro archivo lo invocamos


class CalculadoraAvanzada:
    def sumar_doble(self, a, b):
        return (a + b) * 2
    def saludar(self):
       print("calculadora lista para usar")

from modelos import CalculadoraAvanzada
calculadora = CalculadoraAvanzada()
resultado = calculadora.sumar_doble(3, 4)    
print(f"El resultado de la suma doble es {resultado}")   

# ## otra forma 
#   from modelos import *

# ## * ejercicio:
# modulo de pyhton que genera numeros aleatorios ("ramdom ") para probar las formas de importacion

import math as matematicas
import random 
numero_aleatorio = random.randint(1, 10)
print (f"El numero aleatorio generado es {numero_aleatorio}")

lista =["Ana", "luis", "carlos"]
nombre_aleatorio = random.choice(lista)
print(f"El nombre del ganador es: {nombre_aleatorio}")

prueba = matematicas.ceil(4.2)
print(f"El resultado de redondear hacia el mayor es {prueba}")

###*** Nota siempre se empieza con las importacionesde librerias

