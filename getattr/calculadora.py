class Calculadora:
    def soma(self, num1, num2):
        return num1 + num2

    def sub(self, num1, num2):
        return num1 - num2

    def mult(self, num1, num2):
        return num1 * num2

    def div(self, num1, num2):
        return num1 / num2

    def pow(self, num1):
        return num1 ** 2

class CalculadoraQuebrada:

    def __init__(self):
        self.c = Calculadora()

    def __getattr__(self, n):
        return getattr(self.c, n)

cal = CalculadoraQuebrada()
print(cal.pow(10))
