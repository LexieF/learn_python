class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def perimetro(self):
        return self.lado * 4

    def area(self):
        return self.lado * self.lado

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def perimetro(self):
        return self.altura * 2 + self.base * 2

    def area(self):
        return self.base * self.altura