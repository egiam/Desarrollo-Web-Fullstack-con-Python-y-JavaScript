import datetime

#A traves del radio de un circulo q calcule el area


#a traves de n q haga n + nn + nnn

n = float(input("Coloque un numero: "))

res = n + n*n + n*n*n

print(res)

#Aceptar cadena, contar tamanio y cuantas veces aparece a

cad = input("Escriba algo: ")
tam = len(cad)

print(f"tamanio: {tam}")

#i = 0
cont = cad.count("a") + cad.count("A")
        
print(f"cantidad de a: {cont}")

#Mostrar hora actual con suma de +2hs

hora = datetime.datetime.now().hour + 2

print(f"Hora: {hora}")


