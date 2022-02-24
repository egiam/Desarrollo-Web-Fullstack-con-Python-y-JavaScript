
#Secuencias de datos

#Lista
nombres = ["Harry", "Ron", "Hermione"]
print(nombres)

print(nombres[2]) # 0 | 1 | 2 | etc

nombres.append("Draco") #Agregar a la cadena

nombres.sort() #Orden ascendente

#Tuplas
tupla = (12.5, 1200) 

#Sets
set = set()
set.add("Harry") #Agregar elemento
set.add("Ron")
set.add("Draco")
#SI se repite un elemento, no se agrega, solo queda uno
#No se pueden ordenar, son inmutables

set.remove("Draco") #Remover elemento

#Diccionarios
#No ordenables pero si mutables.

dic = {"clave":"valor", "clave2":"valor2"}
casas = {"Harry":"Gryffindor", "Draco":"Slytherin"}

casas["Hermione"] = "Gryffindor" #Agregar

#-------------------------------

#Toma de desiciones
#~ Invierte los bits (pasa de 0 a 1 y viceversa)

miVar = int(input("Ingrese un digito: "))

if miVar < 0:
    print("La variable es negativa.")
elif miVar == 0:
    print("La variable es cero.")
else:
    print("La variable es positiva")
    
    
print("Es menos que cero") if miVar < 0 else print("Es cero o mayor a cero")

#-------------------------------

for i in range(len(casas)):
    print(i, casas[i])
    if casas[i] == "Slytherin" | casas[i] == "slytherin":
        break
    

