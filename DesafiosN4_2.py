
class Vehiculo:
    
    def capacidad(self, capacidad = 6):
        self.capacidad = capacidad


class Minibus(Vehiculo):
    
    def __init__(self, pasajeros = 0):
        self.pasajeros = pasajeros
    
    def SubePasajero(self):
        if self.pasajeros > 50 | self.pasajeros > self.capacidad:
            print("No hay lugar para mas pasajeros")
        else:
            self.pasajeros += 1
            
    def BajaPasajero(self):
        self.pasajeros -= 1
        
    def __str__(self):
        return f"Se encuentrar {self.pasajeros} pasajeros en el bus. Con una capacidad de {self.capacidad}"


Juan = Minibus(2).capacidad(45)
for i in range(45):
    Vero = Minibus(2).SubePasajero()
    
print(Juan)



