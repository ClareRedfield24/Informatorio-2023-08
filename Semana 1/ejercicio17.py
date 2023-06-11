#Escribe un programa que solicite al usuario dos palabras y luego las imprima en orden inverso.
#Por ejemplo, si el usuario ingresa "hola" y "mundo", el programa debe imprimir
#"mundo hola".
#Importante!!! Utiliza un solo print()

pal1 = input("Por favor ingrese una palabra: ")
pal2 = input("Por favor ingrese otra palabra: ")

print(pal2,pal1)

#otra forma de hacerlo seria

frase = input("Ingrese dos palabras: ")
pal_1,pal_2 = map(str,frase.split(" "))
print(pal_2, pal_1)
