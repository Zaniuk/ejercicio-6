"""
En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:

Color

Ruedas

Puertas

Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:

Velocidad

Cilindrada

Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.
"""

class Vehiculo(): 
    color = ''
    ruedas = 0
    puertas = 0
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas


class Coche(Vehiculo):
    velocidad = 0
    cilindrada = 0
    def __init__(self, velocidad, cilindrada, color, ruedas, puertas ):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

c = Coche(350, 8000, 'Negro', 4, 4)
print(
    "Color: ", c.color, '\n',
    "Velocidad máxima: ", c.velocidad, '\n',
    "Cilindrada: ", c.cilindrada, '\n',
    "Cantidad de ruedas: ", c.ruedas, '\n',
    "Cantidad de puertas: ", c.puertas
    )