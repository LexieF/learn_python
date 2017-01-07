#!/usr/bin/python
#  -*- coding: latin-1 -*-

import unittest
class NumeroPar:
    def __init__(self):
        pass

    def verificar(self, n):
        if n == 0:
            return 'Nulo'
        if n % 2 == 0:
            return True


#n = NumeroPar(2)
#print(n.verificar())

class TestNumeroPar(unittest.TestCase):

#Metodo setUp é o primeiro a ser executado
    def setUp(self):
        self.numero = NumeroPar()

#Metodo tearDown é o ultimo a ser executado em cada teste
    def tearDown(self):
        self.numero = None

    def teste_cinquenta(self):
        self.assertEquals(True, self.numero.verificar(151))

    def teste_zero(self):
        self.assertEquals('Nulo', self.numero.verificar(0))

if __name__ == '__main__':
    unittest.main()