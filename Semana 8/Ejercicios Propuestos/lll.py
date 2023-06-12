class Auto:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

class Camioneta:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

class Bicicleta:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

class Motocicleta:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

vehiculos = []

auto1 = Auto("Ford", "Mustang")
auto2 = Auto("Chevrolet", "Camaro")
camioneta = Camioneta("Toyota", "Hilux")
vehiculo = Vehiculo("Honda", "Civic")
bicicleta1 = Bicicleta("Trek", "Mountain Bike")
bicicleta2 = Bicicleta("Giant", "Trance")
motocicleta = Motocicleta("Yamaha", "YZF-R6")

vehiculos.extend([auto1, auto2, camioneta, vehiculo, bicicleta1, bicicleta2, motocicleta])

# Imprimir la lista de vehículos
for vehiculo in vehiculos:
    clase = vehiculo.__class__.__name__
    atributos = vars(vehiculo)
    print("Clase:", clase)
    print("Atributos:", atributos)
    print("----------------------")
