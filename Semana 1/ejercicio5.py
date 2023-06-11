#Crea un programa que pida al usuario dos numeros enteros y muestre en 
#pantalla su cociente y su resto

num1 = int(input("Por favor ingrese un numero:"))
num2 = int(input("Por favor ingrese otro numero:"))

cociente = num1 // num2 
resto = num1 % num2
print("El cociente entre num1 y num2 es:", cociente)
print("El resto entre num1 y num2 es:", resto)

