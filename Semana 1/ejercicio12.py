#Escribe un programa que solicite al usuario su fecha de nacimiento en formato
#dd/mm/aaaa y luego imprima su edad en anios.Utiliza la funcion .split()
import datetime

fecha_nac = input("Ingrese su fecha de nacimiento en formato dd/mm/yyyy:")
dia, mes, anio = map(int, fecha_nac.split("/"))

fecha_actual = datetime.date.today()
anio_hoy = fecha_actual.year
mes_hoy = fecha_actual.month
dia_hoy = fecha_actual.day

edad = anio_hoy - anio

if(mes > mes_hoy):
    print("Tu edad actual es de:", edad, "anios")
elif((mes == mes_hoy) and (dia == dia_hoy)):
    print("Feliz cumple numero", edad,"!")
elif((mes == mes_hoy) and (dia < dia_hoy)):
    print("feliz cumple numero", edad, "atrasado")
elif((mes == mes_hoy) and (dia <= dia_hoy+3)):
    print("falta poco para tu cumple numero", edad)
else:
    edad -= 1
    print("Tu edad es de:",edad)




