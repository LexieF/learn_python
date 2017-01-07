# Classe que não sabe subtrair mas faz atraves do Decorator
class Operacao:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def operar(funcao):
        def subtrair(self):
            return self.x - self.y

        return subtrair

    @operar
    def fazer_operacao(self):
        return self.y - self.x


op = Operacao(5, 8)
print(op.fazer_operacao())
