#Escribe un programa que solicite al usuario un número decimal y luego imprima la 
#parte entera y decimal por separado

num = input("Por favor ingrese un numero decimal: ")
lista = num.split(".")

print("La parte entera es igual a:",lista[0],"y la parte decimal es:",lista[1])