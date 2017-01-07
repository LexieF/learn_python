def isPrimo(n):
    for i in range(3, n):
        if n % i == 0:
            return False
        return True

def gerarPrimos(n):
    while True:
        if isPrimo(n):
            yield n
        n += 1

primo = gerarPrimos(1)
print(next(primo))
print(next(primo))
print(next(primo))
print(next(primo))
print(next(primo))

