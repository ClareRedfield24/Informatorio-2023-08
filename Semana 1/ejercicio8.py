#Crea un programa que pida al usuario el radio de un círculo y muestre su diámetro, 
#su circunferencia y su área. Supón que pi es aproximadamente 3.14159

pi = 3.14159

r = float(input("Por favor ingrese el valor del radio su circulo:"))
d = float(r*2)
c = float(pi*d)
a = float(pi*(r**2))

print("El valor del diametro es:",d)
print("El valor de su circunferencia es:",c)
print("El valor de su area es:",a)
