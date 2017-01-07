class Relogio:
    def __init__(self, hora, min, seg):
        self.hora = hora
        self.min = min
        self.seg = seg

    def tick(self):
        if (self.seg == 59):
            self.seg = 0
            if (self.min == 59):
                self.min = 0
                if (self.hora == 24):
                    self.hora = 0
                else:
                    self.hora += 1
            else:
                self.min += 1
        else:
            self.seg += 1

    def __str__(self):
        return "{0:02d}:{1:02d}:{2:02d}".format(self.hora, self.min, self.seg)

class Calendario:
    dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    def __init__(self, dia, mes , ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def avancar(self):
        if(self.dia == Calendario.dias[self.mes - 1]):
            self.dia = 1
            if (self.mes == 12):
                self.mes = 1
                self.ano += 1
            else:
                self.mes += 1
        else:
            self.dia += 1

    def __str__(self):
        return "{0:02d}/{1:02d}/{2:4d}".format(self.dia, self.mes, self.ano)


class CalendarioRelogio(Relogio, Calendario):

    def __init__(self, hora, min, seg, dia, mes, ano):
        Relogio.__init__(self, hora, min, seg)
        Calendario.__init__(self, dia, mes, ano)

    def __str__(self):
        return Relogio.__str__(self)+' - '+Calendario.__str__(self)

    def tick(self):
        Relogio.tick(self)
        if self.hora == 24:
            self.hora = 0
            Calendario.avancar(self)

cr = CalendarioRelogio(0, 0, 0, 31, 12, 2016)
for i in range(2678401):
    print(cr)
    cr.tick()
