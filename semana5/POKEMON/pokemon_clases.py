import pokedex
from abc import ABC, abstractmethod

class Pokemon(ABC):
    def __init__(self, nombre, hp_actual, hp_maximo, energia_actual, energia_maxima):
        self.nombre = nombre
        self.hp_actual = hp_actual
        self.hp_maximo = hp_maximo
        self.energia_actual = energia_actual
        self.energia_maxima = energia_maxima

## Aca se define que las propiedades sean privadas
    @property
    def hp_actual(self):
        return self.__hp_actual

    @property
    def hp_maximo(self):
        return self.__hp_maximo
    
    @hp_maximo.setter
    def hp_maxino(self,valor):
        self.hp_maximo = valor

    @property
    def energia_actual(self):
        return self.energia_actual
    
    @property
    def energia_maxima(self):
        return self.energia_maxima
    
    @energia_maxima.setter:
    def energia_maxima(self, valor):
        self.energia_maxima = valor

    def @abstractmethod

class PokemonAgua:

    


print(pokedex.mostrar_catalogo_disponible())



