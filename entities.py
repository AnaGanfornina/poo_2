from datetime import date
from enum import Enum
from random import randint

class Sexo(Enum):
    MASCULINO = 1
    FEMENINO = 2
    NOBINARIO = 3

class Person:
    def __init__(self):
        self.nombre = ""
        self.apellidos = ""
        self.fecha_nacimiento = date.today()
        self.sexo = Sexo(randint(1,3))
        self.dni = ""

    def nombre_completo(self)->str:
        return f"{self.nombre} {self.apellidos}"
    def edad(self)->int:
        return date.today() - self.fecha_nacimiento
    
    def presentarme(self)->str:
        return f"Hola, me llamo {self.nombre} y tengo {self.edad()}"