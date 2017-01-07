import heapq
class FilaDePrioridade:
    def __init__(self):
        self.fila = []
        self.indice = 0

    def push(self, item, prioridade):
        """Imserir elementos no item"""
        heapq.heappush(self.fila,(prioridade, self.indice, item))

    def pop(self):
        """remover elementos do item"""
        return heapq.heappop(self.fila)[-1]


class Item:
    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return self.nome


fila = FilaDePrioridade()
fila.push(Item('marcos'), 28)
fila.push(Item('maria'), 42)
fila.push(Item('marcia'), 67)
print(fila.pop())
print(isinstance(fila, object))
