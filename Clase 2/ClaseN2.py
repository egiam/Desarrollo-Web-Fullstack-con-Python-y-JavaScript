print("Hola Mundo")
print(2 + 2)

numero = 4

#Transformarlo a hexadecimal
print(hex(numero))

#Transformarlo a octal
print(oct(numero))

#Transformarlo a binario
print(bin(numero))

#Transformarlo a String
print(str(numero))

#-------------------------------

#Numeros complejos
numcomplejo = 4 + 1j
print(numcomplejo.imag)
print(numcomplejo.real)

miBoolean = 1 > 2 #False
miBoolean = 1 < 2 #True

#-------------------------------

#Cadenas
miString = "Hello World"
miString = "Godbay good day"
miString = "1234"
print(int(miString)) #Convertir la cadena a int
print(float(miString)) #Convertir la cadena a float

#Funcionalidades de la cadena
print(miString.capitalize())
print(miString.lower())
print(miString.upper())

#Acceder a un elemento particular de la misma
print(miString[1])

#-------------------------------
import datetime

miFechayHora = datetime.datetime.now()
Fecha = datetime.datetime.date()

print(miFechayHora)


