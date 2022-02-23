"""
#Excepciones
import sys #importante para salir del programa, utilizar el system

try:
    numero1 = int(input("Ingrese numero 1: "))
    numero2 = int(input("Ingrese numero 2: "))
except ValueError:
    print("Error. Valor no valido.")
    sys.exit(1)
    
try:
    resultado = numero1 / numero2
except ZeroDivisionError:
    print("Error. No se puede dividir por cero.")
    sys.exit(1)
else:
    print(f"La division salio como esperado.\n El resultado es {resultado}")


#-------------------------------
#Abrir otro archivo?
try:
    f = open("ClaseN3.txt","w")
except FileNotFoundError:
    print("El archivo no se ha encontrado.")
except:
    print("Algo malo paso al intentar abrir el archivo")
finally:
    print("El try y except finalizado.")
  
"""
#-------------------------------

#POO en python

class Perro:
    
    especie = "Canis Lupus Familiaris"
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    #def descripcion(self):
    #    return f"{self.nombre} tiene {self.edad}"
    
    def ladrar(self, sonido):
        return f"{self.nombre} hace este sonido: {sonido}"
    
    def __str__(self):  #Lo q muestra en un simple print
        return f"{self.nombre} has {self.edad} years and is a {Labrador.raza}"
        

class DogoArgentino(Perro):
    pass

class BullDogFrances(Perro):
    pass

class Labrador(Perro):
    raza = "Labrador"


#Africa = Perro("Africa", 15)
Africa = Labrador("Africa", 15)

print(Africa)
