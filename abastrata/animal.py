from abc import ABCMeta, abstractmethod
class Animal(metaclass=ABCMeta):
    @abstractmethod
    def dizer_algo(self):
        return 'Animal disse'

class Cachorro(Animal):
    def dizer_algo(self):
        return super().dizer_algo() + 'AU AU'

c = Cachorro()
print(c.dizer_algo())