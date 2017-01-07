class Nome:
    def __init__(self, nome):
        self.nome = nome

    @property
    def getNome(self):
        return self.nome

    @classmethod
    def criarSobreNome(cls, sobrenome):
        sb = cls(sobrenome)
        return sb

    @staticmethod
    def formatarNomeCompleto(nome, sobrenome):
        if Nome.verificarNome(nome) and Nome.verificarNome(sobrenome):
            return nome+ ' ' +sobrenome

    @staticmethod
    def verificarNome(nome):
        if len(nome) > 0:
            return True

nome = Nome('Fabio')
sobrenome = nome.criarSobreNome('Rolim')
print('Nome completo: %s ' % Nome.formatarNomeCompleto(nome.getNome, sobrenome.getNome))