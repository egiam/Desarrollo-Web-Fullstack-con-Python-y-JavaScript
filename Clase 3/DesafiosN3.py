
#Si a es mayor a b, imprimir hola mundo
a = 11
b = int(input("Coloque un numero entero: "))

if a > b:
    print("Hola Mundo")

#Programa q acepte 5 decimales
lista = []

for i in range(5):
    lista.append(float(input(f"Coloque el {i+1} numero: ")))
    
print(lista)

#Guardar en lista 5 numeros recibidos. Recorrer la lista y mostrar cada numero x pantalla
#Se usa lo de arriba
for i in range(len(lista)):
    print(lista[i])


#Dada la lista, mostrar numeros divisibles x 5, 
#si encuentra numero mayor a 150 haga break.
lista1 = [12,15,32,42,55,75,122,132,150,183,190]

for i in range(len(lista1)):
    if lista1[i] > 150:
        break
    if lista1[i]%5 == 0:
        print(lista1[i])

