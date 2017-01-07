import json
class Contato:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    @property
    def oberterDados(self):
        return ('{} {}'.format(self.nome, self.sobrenome))


c = Contato('Fabio', 'Rolim')
print(c.oberterDados)
dump = json.dumps(c.__dict__)
print(dump)