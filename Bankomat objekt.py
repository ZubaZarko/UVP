class Banka:

    def __init__(self, stanje, transakcije):
        self.stanje = 0
        self.transakcije = []

    def __str__(selfself):
        return('Stanje na vasem racunu: {}€').format(self.stanje)

    def dvig(self, znesek):
        if znesek > self.stanje:
            self.transakcije.append('zavrnjen dvig zneska {}€').format(znesek)
            return('Stanje na vasem racunu je prenizko')

        else:
            self.stanje -= znesek
            self.transakcije.append(self.stanje)
            return('Dvig uspesen')

    def polog(self, koliko):
        self.stanje += koliko
        return self.stanje