# Nos piden que diseñemos un programa para gestionar donaciones de alimentos.
# Los productos tienen los siguientes atributos:
# Nombre
# Cantidad
#Tenemos dos tipos de productos:
#Perecedero: tiene un atributo llamado días a caducar.
#No perecedero: tiene un atributo llamado tipo.
# Tendremos una función llamada Calcular, que según cada clase hará una cosa u
# otra, a esta función se le envía la cantidad por producto y entidades a las cuáles
# se entregarán donaciones
# Debe obtener la cantidad que se enviará a cada entidad, sabiendo que la
# distribución debe ser lo más equitativa posible. En caso que sobren
# productos, se almacenan para el próximo ciclo de donación.
# Además si el producto es perecedero, se informará:
# Si le queda menos de 10 días para caducar, la entrega debe hacerse en el
# día actual.
# Si le queda 1 mes para caducar, la entrega debe hacerse en el plazo de 1
# semana.
# Si fuera No Perecedero, se informa cuántos productos se entregarán por
# entidad y que queda libre la elección de la fecha de entrega siempre que no
# supere el mes.

class Productos:
    def __init__(self, nombre, cantidad):
        self.nombre= nombre
        self.cantidad= cantidad

class Producto_Perecedero(Productos):
    def __init__(self, nombre, cantidad, dias_caducar):
        super().__init__(nombre, cantidad)
        self.dias_caducar= dias_caducar
        
    def Calcura_entrega(self, entidades):
        if self.dias_caducar < 10:
            print(f"Los productos {self.nombre} deben entregarse hoy a las entidades {entidades}")
        if self.dias_caducar < 30:
            print(f"Los productos {self.nombre} deben entregarse hoy el plazo de una semana a las entidades {entidades}")
        else:
            self.entregar_productos(entidades)

    def entregar_productos(self, entidades):
        cantidad_por_entidad = self.cantidad // len(entidades)
        sobrante = self.cantidad % len(entidades)

        for entidad in entidades:
            print(f"Se entregarán {cantidad_por_entidad} {self.nombre} a la entidad {entidad}.")

        if sobrante > 0:
            print(f"Quedan {sobrante} {self.nombre} para el próximo ciclo de donación.")

class NoPerecedero(Productos):
    def __init__(self, nombre, cantidad, tipo):
        super().__init__(nombre, cantidad)
        self.tipo = tipo

    def calcular_entrega(self, entidades):
        cantidad_por_entidad = self.cantidad // len(entidades)
        sobrante = self.cantidad % len(entidades)

        for entidad in entidades:
            print(f"Se entregarán {cantidad_por_entidad} {self.nombre} a la entidad {entidad}.")

        if sobrante > 0:
            print(f"Quedan {sobrante} {self.nombre} para el próximo ciclo de donación.")


entidades = ["Entidad A", "Entidad B", "Entidad C"]
perecedero = Producto_Perecedero("Leche", 100, 7)
no_perecedero = NoPerecedero("Arroz", 500, "Grano")

perecedero.Calcura_entrega(entidades)
print()
no_perecedero.calcular_entrega(entidades)

