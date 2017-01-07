class Numero():
    def __init__(self, x):
        self.x = x

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, num):
        if (num > 0):
            self._x = num


n = Numero(14)
print(n.x)
n.x = -1
print(n.x)