def meu_decorator(fat):
    def fat(x):
        f = x
        while x > 1:
            f = f * (x - 1)
            x -= 1
        return f
    return fat

@meu_decorator
def dobro(x):
    return 2 * x

print(dobro(5))