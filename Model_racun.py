class Racun:
    stanje=0
    stavilka_racuna='' 

    def __init__(self, stevilka_racuna):
        self.stevilka_racuna = stevilka_racuna
        self.stanje = 0
        with open(stevilka_racuna) as racun:
            for vrstica in racun:
                self.stanje = float(vrstica.split(',')[1].strip())

    def __repr__(self):
        return('Stanje na vasem racunu: {}€').format(self.stanje)

    def preveri_stanje(self, st_racuna):
        print('Stanje na vasem racunu: {}€').format(self.stanje)

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


