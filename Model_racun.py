class Racun:

    def __init__(self, pin):
        self.stanje = 0
        self.transakcije = []
        self.pin = pin

    def __str__(self):
        return('Stanje na vasem racunu: {}€').format(self.stanje)

    def dvig(self, znesek):
        if znesek > self.stanje:
            return('Stanje na vasem racunu je prenizko')

        else:
            self.stanje -= znesek
            self.transakcije.append(self.stanje)
            return('Dvig uspesen')

    def polog(self, koliko):
        self.stanje += koliko
        return self.stanje

    def transakcija(self, racun, kolicina):
        if self.stanje < kolicina:
            return('Transkacija na {} zavrnjena').format(racun)
        else:
            self.stanje -= kolicina
            self.transakcije.append(self.stanje)
            racun.stanje += kolicina
            racun.transakcije.append(racun.stanje)
            return('Transakcija uspesna')

    def izpis_prometa(self):
        return self.transakcije


