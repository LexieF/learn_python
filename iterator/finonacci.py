class Fibonacci():
    def __init__(self, max):
        self.max = max


    def __iter__(self):
        self.x, self.y = 1, 1
        return self

    def __next__(self):
        fib = self.x
        if fib > self.max:
            raise StopIteration
        else:
#            self.x = self.y
#            self.y = self.x + self.y
            self.x, self.y = self.y, self.x + self.y
        return fib

f = Fibonacci(100)
for i in f:
   print(i, end = ' ')
