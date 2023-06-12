# Ejercicio 1: Vehículo pt.1
# A partir del siguiente diagrama de clases, implementá
# clases y métodos para mostrar atributos.

class Vehiculo:
    #constructor
    def __init__(self, color, ruedas): #cuando se usa el self como parametro se esta pasando la clase misma
        self.color= color
        self.ruedas= ruedas

    def Presentar(self):
        return f"El coche es de color {self.color} y tiene ruedas de {self.ruedas}"

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad= velocidad
        self.cilindrada= cilindrada
#metodos
    def tipo_coche(self):
        return f"Mi coche es de color {self.color}, tiene una cilindrada de {self.cilindrada} cc, {self.ruedas} ruedas y una velocidad de {self.velocidad} km/h"
        
mi_coche = Coche("Rojo",4, 170, 200)
print(mi_coche.tipo_coche())

