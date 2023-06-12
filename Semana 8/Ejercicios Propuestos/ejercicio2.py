# Ejercicio 2:
# Vehículo pt.2
# Crea al menos un objeto de cada subclase y añádelos a una lista llamada vehículos
# Realiza una funciónllamada catalogar() que reciba la lista de vehículos y los recorra
# mostrando el nombre de su clase y sus atributos.
# Modifica la función catalogar() para que reciba un argumento optativo
# ruedas, haciendo que muestre únicamente los que su número de ruedas
# concuerde con el valor del argumento. También debe mostrar un mensaje "Se
# han encontrado {} vehículos con {} ruedas:" únicamente si se envía el
# argumento ruedas. Ponla a prueba con 0, 2 y 4 ruedas como valor.

vehiculos =[]

class Vehiculo:
    #constructor
    def __init__(self, color, ruedas): #cuando se usa el self como parametro se esta pasando la clase misma
        self.color= color
        self.ruedas= ruedas

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad= velocidad
        self.cilindrada= cilindrada

class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas,velocidad, cilindrada)
        self.carga= carga

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo= tipo

    
class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad= velocidad
        self.cilindrada= cilindrada


vehiculo= Vehiculo("Rojo", 4)
coche= Coche("Verde", 4, 170, 200)
bici=Bicicleta("Azul", 2, "Urbana")
moto= Motocicleta("Celeste", 4, "Deportiva", 100, 150)
camioneta=Camioneta("Negra",4, 200, 300, 1500)

vehiculos.extend([vehiculo,coche,bici,moto,camioneta])


# for vehiculo in vehiculos:
#     print(f"Clase: {vehiculo.__class__.__name__}\nAtributos: {vars(vehiculo)}") 

def catalogar(vehiculos, ruedas=None):
    vehiculos_filtrados = []
    
    for vehiculo in vehiculos:
        if ruedas is None or getattr(vehiculo, 'ruedas', None) == ruedas:
            vehiculos_filtrados.append(vehiculo)
    
    if ruedas is not None:
        return f"Se han encontrado {len(vehiculos_filtrados)} vehículos con {ruedas} ruedas:"

print(catalogar(vehiculos,0))



