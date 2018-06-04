class Racun: 

    def __init__(self, stevilka_racuna):
        self.stevilka_racuna = stevilka_racuna
        self.stanje = 0
        self.transakcije = []
        with open(stevilka_racuna) as racun:
            for vrstica in racun:
                self.stanje = float(vrstica.split(',')[1].strip())

    def __str__(self):
        return('Stanje na vasem racunu: {}€').format(self.stanje)

    def stanje(self):
        with open(self.stevilka_racuna) as racun:
            for vrstica in racun:
                self.stanje = float(vrstica.split(',')[1].strip())

    def dvig(self, znesek):
        if znesek > self.stanje:
            return False
        else:
            self.stanje -= znesek
            with open(self.stevilka_racuna, 'a') as racun:
                print('-{}, {}'.format(znesek, self.stanje), file=racun)
            return True

    def polog(self, koliko):      #ne vem kako ucinkovito pisati v datoteko
        self.stanje += koliko
        with open(self.stevilka_racuna, 'a') as racun:
            print('+{}, {}'.format(koliko, self.stanje), file=racun)

    def nakazi(self, st_prejemnika, kolicina):
        vsi_racuni = []
        with open('uporabniki') as usernames:
            for vrstica in usernames:
                vsi_racuni.append(vrstica[0:20])
        if self.stanje < kolicina:
            print('Stanje na vasem racunu je prenizko')
            return 0
        elif st_prejemnika in vsi_racuni:
            self.dvig(kolicina)
            prejemnik = Racun(st_prejemnika)
            prejemnik.polog(kolicina)
            return 1
        else:
            print('Transakcijska stevilka ne obstaja')
            return 2

    def izpis_prometa(self):
        self.transakcije.clear()
        with open(self.stevilka_racuna) as racun:
            for vrstica in racun:
                self.transakcije.append(vrstica.split(',')[0].strip())
        print(self.transakcije)


