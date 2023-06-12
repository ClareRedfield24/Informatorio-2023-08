# Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que
# es una persona) y cantidad (puede tener decimales). El titular será obligatorio y
# la cantidad es opcional.
# Implementa los siguientes métodos:
# mostrar(): Muestra los datos de la cuenta.
# ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad
# introducida es negativa, no se hará nada.
# retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en
# números rojos.

class Cuenta:
    def __init__(self, titular, cantidad=0):
        self.titular= titular
        self.cantidad= cantidad

    def Mostrar(self):
        return f"Hola! {self.titular} tu saldo restante es de {self.cantidad}"
    
    def Ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
            return f"Ingresaste la cantidad de {self.cantidad} a tu cuenta"
        
    def Retirar(self, cantidad):
        self.cantidad -= cantidad
        return f"Retiraste la cantidad de {self.cantidad} de tu cuenta"
    
cuenta= Cuenta("Claudia Dure", 0)

print(cuenta.Mostrar())

print(cuenta.Ingresar(1000))
print(cuenta.Mostrar())
print(cuenta.Retirar(150))
print(cuenta.Mostrar())

