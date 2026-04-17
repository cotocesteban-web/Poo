import pokedex
from abc import ABC, abstractmethod

class Pokemon(ABC):
    def __init__(self, nombre, hp_actual, hp_maximo, energia_actual, energia_maxima):
        self.nombre = nombre
        self.hp_actual = hp_actual
        self.hp_maximo = hp_maximo
        self.energia_actual = energia_actual
        self.energia_maxima = energia_maxima

   ## funciones del padre
    def defender(self):
        if self.energia_actual >= 5:
            self.energia_actual -= 5
            self.defendiendo = True
            print(f"{self.nombre} se defiende.")
        else:
            print("No hay energia suficiente.")
 #####funcion descanaar
    def descansar(self):
        self.energia_actual += 20
        print(f"{self.nombre} descansa y recupera energía.")

    def recibir_daño(self, daño):
        if self.defendiendo:
            daño = daño // 2
            self.defendiendo = False
        self.hp_actual -= daño
        print(f"{self.nombre} recibe {daño} de daño.")

    # MÉTODO ABSTRACTO
    @abstractmethod
    def atacar(self, oponente):
        pass

## Aca se define que las propiedades sean privadas
    @property
    def hp_actual(self):
        return self.__hp_actual
    
    @hp_actual.setter:
    def hp_actual(self_valor):
    

    @property
    def energia_actual(self):
        return self.energia_actual
    
    @energia_actual.setter
    def energia_actual(self, valor):


   
class PokemonAgua(Pokemon):
    def __init__(self, nombre, hp_maximo, energia_maxima):
        super().__init__(nombre, hp_maximo, energia_maxima)

    def atacar(self, oponente):
        if self.energia_actual < 15:
            print("No hay energa suficiente.")
            return

        self.energia_actual -= 15
        daño = 10





    


print(pokedex.mostrar_catalogo_disponible())



