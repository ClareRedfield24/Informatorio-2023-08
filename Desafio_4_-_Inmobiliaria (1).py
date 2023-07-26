# Desafío 4: La inmobiliaria

def inmuebles_lista_completa(inmuebles):
    print("Lista completa de inmuebles:")
    for i, inmueble in enumerate(inmuebles):
        precio = calcular_precio(inmueble)
        print(f"Inmueble {i+1}: {inmueble} - Precio: ${precio}")


def buscar_inmuebles_por_presupuesto(inmuebles):
    presupuesto = float(input("Ingrese su presupuesto: $"))
    inmuebles_disponibles = []
    for inmueble in inmuebles:
        if inmueble['Estado'] in ['Disponible', 'Reservado']:
            precio = calcular_precio(inmueble)
            if precio <= presupuesto:
                inmueble_con_precio = inmueble.copy()
                inmueble_con_precio['precio'] = precio
                inmuebles_disponibles.append(inmueble_con_precio)
    
    if len(inmuebles_disponibles) == 0:
        print("\nNo hay inmuebles disponibles dentro de su presupuesto.")
    else:
        print("Inmuebles dentro de su presupuesto:")
        for inmueble in inmuebles_disponibles:
            print(inmueble)

def editar_inmueble(inmuebles):
    print("Seleccione el número del inmueble a editar:")
    inmuebles_lista_completa(inmuebles)

    opcion = int(input("Opción: "))
    if opcion < 1 or opcion > len(inmuebles):
        print("¡Opción inválida!")
        return
    
    inmueble = inmuebles[opcion - 1]
    print("Ingrese los nuevos datos del inmueble:")
    inmueble['año'] = int(input("Año: "))
    inmueble['metros cuadrados'] = int(input("Metros cuadrados: "))
    inmueble['habitaciones'] = int(input("Cantidad de habitaciones: "))
    inmueble['garaje'] = input("¿Tiene garaje? (Sí/No): ").lower() == 'sí'
    inmueble['zona'] = input("zona (A/B/C): ").upper()
    
    print("\n¡El Inmueble ha sido actualizado!")

def eliminar_inmueble(inmuebles):
    print("Indique el número del inmueble a eliminar:")
    inmuebles_lista_completa(inmuebles)

    opcion = int(input("Opción: "))
    if opcion < 1 or opcion > len(inmuebles):
        print("¡Opción inválida!")
        return
    
    inmuebles.pop(opcion - 1)
    print("\n¡El Inmueble ha sido eliminado!")


def cambiar_estado_inmueble(inmuebles):
    print("Seleccione el inmueble a cambiar de estado:")
    inmuebles_lista_completa(inmuebles)

    opcion = int(input("Opción: "))
    if opcion < 1 or opcion > len(inmuebles):
        print("¡Opción inválida!")
        return
    
    inmueble = inmuebles[opcion - 1]
    nuevo_estado = input("Ingrese el estado a cambiar: (Disponible/Reservado/Vendido): ").capitalize()
    if nuevo_estado not in ['Disponible', 'Reservado', 'Vendido']:
        print("¡Estado inválido!")
        return
    
    inmueble['Estado'] = nuevo_estado
    print("\n¡Estado del inmueble actualizado!")

def agregar_inmueble(inmuebles):
    inmueble_nuevo = {}

    inmueble_nuevo['año'] = int(input("Año de construcción: "))
    inmueble_nuevo['metros cuadrados'] = int(input("Metros cuadrados: "))
    inmueble_nuevo['habitaciones'] = int(input("Número de habitaciones: "))
    tiene_garaje = input("¿Tiene garaje? (Si/No): ").lower()
    inmueble_nuevo['garaje'] = tiene_garaje == 'si'
    inmueble_nuevo['zona'] = input("zona (A, B, C): ").upper()
    inmueble_nuevo['Estado'] = 'Disponible'

    if validar_inmueble(inmueble_nuevo) == True:
        inmuebles.append(inmueble_nuevo)
        print("\n¡El Inmueble ha sido agregado!")
    else:
        print("\n¡El inmueble no puede ser añadido a la lista!")

def validar_inmueble(inmuebles):
    if inmuebles["año"] < 2000:
        return False
    elif inmuebles["habitaciones"] < 2:
        return False
    elif inmuebles["metros cuadrados"] < 60:
        return False
    zona_valida = ["A", "B", "C"]
    if inmuebles["zona"] not in zona_valida: 
        return False
    
    return True

def calcular_precio(inmueble):
    zona = inmueble['zona']
    metros = inmueble['metros cuadrados']
    habitaciones = inmueble['habitaciones']
    garaje = inmueble['garaje']
    antiguedad = 2023 - inmueble['año']

    if zona == 'A':
        precio = (metros * 100 + habitaciones * 500 + garaje * 1500) * (1 - antiguedad / 100)
    elif zona == 'B':
        precio = (metros * 100 + habitaciones * 500 + garaje * 1500) * (1 - antiguedad / 100) * 1.5
    elif zona == 'C':
        precio = (metros * 100 + habitaciones * 500 + garaje * 1500) * (1 - antiguedad / 100) * 2

    return precio


inmuebles = [
    {'año': 2010, 'metros cuadrados': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'Estado': 'Disponible'},
    {'año': 2016, 'metros cuadrados': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'Estado': 'Reservado'},
    {'año': 2000, 'metros cuadrados': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'Estado': 'Disponible'},
    {'año': 2015, 'metros cuadrados': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'Estado': 'Vendido'},
    {'año': 2008, 'metros cuadrados': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'Estado': 'Disponible'}
]

while True:
    print("--------OPCIONES--------")
    print("1- Mostrar lista completa de inmuebles")
    print("2- Buscar inmuebles por presupuesto")
    print("3- Agregar un inmueble")
    print("4- Editar un inmueble")
    print("5- Eliminar un inmueble")
    print("6- Cambiar el estado de un inmueble")
    print("7- Salir")

    opcion = input("\nSeleccione una opción: ")

    if opcion == '1':
        inmuebles_lista_completa(inmuebles)
    elif opcion == '2':
        buscar_inmuebles_por_presupuesto(inmuebles)
    elif opcion == '3':
        agregar_inmueble(inmuebles)
    elif opcion == '4':
        editar_inmueble(inmuebles)
    elif opcion == '5':
        eliminar_inmueble(inmuebles)
    elif opcion == '6':
        cambiar_estado_inmueble(inmuebles)
    elif opcion == '7':
        break
    else:
        print("¡Opción inválida!")