class Livro():
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

class LivroMixin():
    def mostrarDados(self):
        print(self.nome, self.valor)


class LivroHtml(Livro, LivroMixin):
    pass

l = LivroHtml('Livro de HTML', 50.99)
l.mostrarDados()