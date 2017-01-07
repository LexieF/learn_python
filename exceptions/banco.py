class SaldoInsuficiente(Exception):
    def __init__(self):
        #self.args = 'saldo insuficiente'
        super().__init__('Saldo insuficiente')

def transferencia(valor):
    saldo = 100
    saldo -= valor
    if(saldo > 0):
        return True

try:
    if not transferencia(200):
        raise SaldoInsuficiente()
except SaldoInsuficiente as e:
    print(e.args)