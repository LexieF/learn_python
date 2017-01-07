class FiguraGeometrica():
    def __index__(self, nome):
        self.nome = nome

class Quadrado(FiguraGeometrica):
    def __init__(self, nome, lado):
        FiguraGeometrica.__init__(self)
        self.lado = lado

    def calculaArea(self):
        return self.lado ** 2

class Triangulo(FiguraGeometrica):
    def __init__(self, nome, base, altura):
        FiguraGeometrica.__init__(self)
        self.base = base
        self.altura = altura

    def calculaArea(self):
        return ((self.base * self.altura) / 2)

quad = Quadrado('Quadrado', 10)
print('Area do quadrado: %d' %quad.calculaArea())

tri = Triangulo('Triangulo', 15, 10)
print('Area do triangulo: %d' %tri.calculaArea())

