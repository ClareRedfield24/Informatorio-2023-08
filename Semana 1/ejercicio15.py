#Escribe un programa que solicite al usuario una temperatura en grados Celsius y 
#luego imprima la temperatura equivalente en grados Fahrenheit. La fórmula para 
#convertir de Celsius a Fahrenheit es: F = (C * 1.8) + 32

temp_celcius = float(input("Por favor ingrese el valor de temperatura:"))
temp_fahrenheit = float((temp_celcius*1.8)+32)

print("El valor de su temperatura en grados Fahrenheit es igual a: ",temp_fahrenheit)