import pokedex
from abc import ABC, abstractmethod

class Pokemon(ABC):
    def __init__(self, nombre, hp_actual, hp_maximo, energia_actual, energia_maxima):
        self.nombre = nombre
        self.hp_actual = hp_actual
        self.hp_maximo = hp_maximo
        self.energia_actual = energia_actual
        self.energia_maxima = energia_maxima

    @property
    def hp_actual(self):
        return self.hp_actual

    @property
    def hp_maximo(self):
        return self.hp_maximo

    @property
    def energia_actual(self):
        return self.energia_actual
    
    


print(pokedex.mostrar_catalogo_disponible())



