
class Rectangulo:
    
    def __init__(self, longitud, ancho):
        self.longitud = longitud
        self.ancho = ancho
        
    def __str__(self):
        area = self.longitud * self.ancho
        return f"El area del rectangulo es: {area}cm"


rec = Rectangulo(12,5)

print(rec)

