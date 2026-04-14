# Crear clase inicio
class SensorPresion:
   # atributo de la clase este valor va ser para todos los objetos
    LIMITE_PELIGRO = 200  
    # Contador global de cuantos sensores se van a crear
    total_lecturas = 0    
 ### este es el constructor.
    def __init__(self, nombre, presion):
        ## atributo publico. aca ira el nombre de la caldera
        self.nombre = nombre
        ## este es el atributo privado
        self.__presion = 0 
        ### atributo que se puede modificar
        self.presion = presion  # usa el setter para validar
        # se incrementa el contador globlal cada vez que se crea un sensor
        SensorPresion.total_lecturas += 1

    # Me permite leer la el dato que es la presion sin modificarla directamente
    @property
    def presion(self):
        return self.__presion

    # Setter me permite modificar el dato.
    @presion.setter
    def presion(self, valor):
        # validar que la presion no sea negativa
        if valor >= 0:
            self.__presion = valor
        else:
            # mensaje de error si la presion es invalida
            print(f"Error: La presion es negativa {self.nombre}")

            # se asigna 0 si el valor es incorrecto
            self.__presion = 0


# Crar lista donde se guardan los sensores creados
sensores = []

print("--- Sistema De Monitoreo Industrial ---")
print("Leyendo registros de presion.....")

# mostramos el archivo utilizando "r"
# abrir y cerrar archivo de froma autmomatica con with open y mosttrarla con r
with open("registros.txt", "r") as archivo_entrada:

    # con un ciclo se recorre el archivo linea por linea
    for nombre in archivo_entrada:

        # Strip elimina los saltos de linea o espacio en blanco
        nombre_caldera = nombre.strip()

        # con read line solo se lee una linea utilizando el puente que nos lleva directo a la linea
        presion_caldera = archivo_entrada.readline()

        # si no tenemos mas datos se termina el ciclo
        if not presion_caldera:
            break

        # convertir la presión a entero
        valor_presion = int(presion_caldera.strip())

        # Se crea un objeto SensorPresion con los datos leidos
        nuevo_sensor = SensorPresion(nombre_caldera, valor_presion)

        # se agrega el objeto a la lista
        sensores.append(nuevo_sensor)
    

# iniciar el archivo de salidas 
with open("alertas.txt", "w") as salida:

    # se escribe el encabezado del reporte
    salida.write("Reporte de incidencias\n")

    # contador para numerar las calderas en peligro
    contador_alertas = 0

    # recorrer todos los sensores existentes
    for i in sensores:

        # evaluar si la presion supera el limite
        if i.presion > SensorPresion.LIMITE_PELIGRO:

            # estado peligro
            estado = "!peligro!"

            # incrementar el contador
            contador_alertas += 1

            # escribir en el archivo el nombre de la caldera
            salida.write(str(contador_alertas) + ". " + i.nombre + "\n")
        else:
            # mostrar el estado seguro
            estado = "seguro"

        # mostrar en pantalla el analisis de cada caldera
        print("Analizando: " + i.nombre + "estado: " + estado)

    # Mostrar un mensaje al final del archivo
    salida.write("calderas criticas....\n")


# Mostrar un mensaje si se genero el archivo
print("\n[AUDITORÍA] Se han generado alertas en el archivo 'alertas.txt'")

# mostrar el resumen total de sensores procesados
print(f"[RESUMEN] Total de sensores procesados: {SensorPresion.total_lecturas}.") 



        
    