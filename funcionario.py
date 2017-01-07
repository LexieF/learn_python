class Funcionario():
    def __init__(self, nome, salario, cpf):
        self.nome = nome
        self.salario = salario
        self.cpf = cpf

    def get_bonificacao(self):
        return self.salario * 0.10


class Gerente(Funcionario):

    def __init__(self, nome, salario, cpf, senha):
        super().__init__(nome, salario, cpf)
        self.senha = senha

    def get_bonificacao(self):
        return super().get_bonificacao() + 1000

g = Gerente('Fabio', 6000.00, '123456789', 'oioi')
print(g.get_bonificacao())