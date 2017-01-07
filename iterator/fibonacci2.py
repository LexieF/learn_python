#0s 10 primeiros elementos da fibonacci
def fibonacci(max):
    x, y = 1, 1
    i = 0
    while i < max:
        yield x
        x, y = y , x + y
        i += 1
gerador = fibonacci(10)
print(gerador.__next__())
for i in gerador:
    print(i)
