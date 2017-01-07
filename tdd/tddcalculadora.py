import unittest
from tdd.calculadora import Calculadora


class Tdd(unittest.TestCase):

    def teste_soma(self):
        c = Calculadora()
        self.assertEquals(30, c.somar(10, 20))

    def teste_sub(self):
        c = Calculadora()
        self.assertEquals(-10, c.sub(10, 20))


if __name__ == '__main__':
    unittest
