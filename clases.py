import math as mt
class figuras():
    def __init__(self):
        pass
    def calcularPerimetro():
        pass
    def calcularArea():
        pass

class TrianguloRectangulo(figuras):
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
    def calcularHipotenusa(self):
        return ((self.base)**2 + (self.altura)**2)**0.5
    def calcularArea(self):
        return (self.base*self.altura)/2
    def calcularPerimetro(self,hipotenusa):
        return self.base+self.altura+hipotenusa
    def determinarTipoTriangulo(self,hipotenusa):
        if self.base==self.altura and self.base==hipotenusa:
            print("Es un triángulo equilatero")
        elif self.base!=self.altura and self.base!=hipotenusa:
            print("Es un triángulo escaleno")
        else: print("Es un triángulo isoceles")
class Circulo(figuras):
    def __init__(self,radio):
        self.radio=radio
    def calcularArea(self):
        return mt.pi*self.radio**2
    def calcularPerimetro(self):
        return 2*mt.pi*self.radio
    

class Cuadrado(figuras):
    def __init__(self,lado):
        self.lado=lado
    def calcularArea(self):
        return self.lado*self.lado
    def calcularPerimetro(self):
        return 4*self.lado

class Rectangulo(figuras):
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
    def calcularArea(self):
        return self.base*self.altura
    def calcularPerimetro(self):
        return (2*self.base)+(2*self.altura)

class Rombo(figuras):
    def __init__(self,lado,D,d):
        self.lado=lado
        self.D=D
        self.d=d
    def calcularArea(self):
        return (self.d*self.D)/2
    def calcularPerimetro(self):
        return 4*self.lado