class Pato():
    def quack(self):
        print('quack - quack')

class Pessoa():
    def quack(self):
        print('faco quack igual a um pato')

class Passarinho():
    def cantar(self):
        print('Passarinho não faz quack igual a um pato')

def tentar_fazer_quack(obj):
    try:
        obj.quack()
    except Exception as e:
            print(e)

pessoa = Pessoa()
pato = Pato()
passarinho = Passarinho()
tentar_fazer_quack(pessoa)
tentar_fazer_quack(pato)
tentar_fazer_quack(passarinho)
