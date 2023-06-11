#Crea un programa que pida al usuario una cantidad en dólares y la convierta a euros.
#Supón que el tipo de cambio es de 0.84 euros por dólar.

dolares = float(input("Por favor ingrese su valor en dolares:"))

euros = float(dolares*0.84)

print("Su valor en euros es:",euros)