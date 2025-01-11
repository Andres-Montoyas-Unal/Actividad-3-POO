
class Triangulo():
    def __init__(self,lado):
        self.lado=lado
    def calcular_area(self,lado):
        return int(lado)**2/2
    def calcular_perimetro(self,lado):
        return int(lado)*3
    def calcular_altura(self,lado):
        return(int(lado)*(3)**0.5)/2


        
