from tkinter import *
from Model_racun import *


class Bankomat_vmesnik():

	def __init__(self, okno):

		self.prijava = Frame(okno, background='palegreen')

		self.obvestilo = Label(self.prijava, font="Gill_Sans 30 bold", text='Pozdravljeni v Piton banki!', background='palegreen')
		self.vpisi_pin = Label(self.prijava, font="Gill_Sans 16" , text='Tukaj vnesite svojo PIN kodo:', background='palegreen')
		self.vnos_pin = Entry(self.prijava, justify='center',font="Gill_Sans 20 bold", width=6, show='•', background='lightgray')
		self.potrdi_pin = Button(self.prijava, font="Gill_Sans 18 bold", text='POTRDI', command=self.preveri_pin, background='palegreen')


		self.glavno_okno = Frame(okno)

		self.napis = Label(self.glavno_okno, font='Gill_Sans 8', text='Banka Piton Inc., ATM num.: 322112')
		self.izhodni_podatki = DoubleVar(okno) #tuki nastavim kaj je se izpise na oknu
		self.vnos = Label(self.glavno_okno, font='Gill_Sans 12 bold', text='Vnesi znesek:')
		self.display = Entry(self.glavno_okno, justify='center', background='powderblue',
			width=40, font='16', textvariable=self.izhodni_podatki)
		self.vnos_zneska = Entry(self.glavno_okno, justify='center')
		self.okno_nakazilo = Entry(self.glavno_okno, justify='center')
		self.gumb_polog = Button(self.glavno_okno, text='polog', command=self.polozi)
		self.gumb_dvig = Button(self.glavno_okno, text='dvig', command=self.dvigni)
		self.gumb_stanje = Button(self.glavno_okno, text='preveri stanje', command=self.preveri_stanje)
		self.gumb_transakcije = Button(self.glavno_okno, text='preveri transakcije', command=self.izpisi_transkacij)
		self.gumb_nakazilo = Button(self.glavno_okno, text='poslji nakazilo', command=self.nakazilo)
		self.gumb_izhod = Button(self.glavno_okno, text='odjava', command=self.izhod)

		self.obvestilo.pack()
		self.vpisi_pin.pack()
		self.vnos_pin.pack() 
		self.potrdi_pin.pack()
		self.prijava.pack()

		self.napis.grid(row=0, column=0)
		self.display.grid(row=1, column=1, columnspan=4)
		self.vnos.grid(row=2, column=1)
		self.vnos_zneska.grid(row=2, column=1, columnspan=4)
		self.gumb_polog.grid(row=3, column=3)
		self.gumb_dvig.grid(row=4, column=3)
		self.gumb_stanje.grid(row=3, column=2)
		self.gumb_transakcije.grid(row=4, column=2)
		self.okno_nakazilo.grid(row=6, column=1, columnspan=3)
		self.gumb_nakazilo.grid(row=6, column=3)
		self.gumb_izhod.grid(row=8, column=5)

	def preveri_pin(self):
		if self.vnos_pin.get() == '':
			return None
		pin = int(self.vnos_pin.get())
		with open('uporabniki') as usernames:
			for vrstica in usernames:
				if int(vrstica[22:26]) == pin:
					st_racuna = vrstica[0:20]
					print(vrstica[0:20])
					print('PIN koda pravilna')
					self.prijava.pack_forget()
					self.glavno_okno.pack()
					self.racun = Racun(st_racuna)###tole povzroci da on zacn delovat kot objekt, skrit pod st. racuna
					self.izhodni_podatki.set(str(self.racun.stevilka_racuna))
				else:
					pass
			return self.vnos_pin.delete(0, END)

	def polozi(self):##tezeva z zapisovanjem v file, brise mi starega
		if self.vnos_zneska.get() == '':
			return self.izhodni_podatki.set('Najprej vnesite zeljeni znesek')
		self.racun.polog(float(self.vnos_zneska.get()))
		self.izhodni_podatki.set('Polog uspesen!')
		return self.vnos_zneska.delete(0, 'end')

	def dvigni(self):
		if self.vnos_zneska.get() == '':
			return self.izhodni_podatki.set('Najprej vnesite zeljeni znesek')
		elif self.racun.dvig(float(self.vnos_zneska.get())):
			return self.izhodni_podatki.set('Dvig uspesen!')
		else:
			self.izhodni_podatki.set('Stanje na vasem racunu je prenizko!')
		return self.vnos_zneska.delete(0, 'end')

	def preveri_stanje(self):
		self.izhodni_podatki.set('Stanje na vasem racunu je {}€'.format(self.racun.stanje))
		

	def izpisi_transkacij(self):
		self.racun.izpis_prometa()
		self.izhodni_podatki.set(", ".join([str(x) for x in self.racun.transakcije]))	#ustvari niz z elementi sez.
		return self.vnos_zneska.delete(0, 'end')																				#in elemente loci z ", "

	def nakazilo(self):
		if self.vnos_zneska.get() == '':
			return self.izhodni_podatki.set('Vnesite zeljeni znesek!')
		elif self.okno_nakazilo.get() == '':
			return self.izhodni_podatki.set('Vnesite stevilko racuna prejemnika!')
		elif self.racun.nakazi(self.okno_nakazilo.get() ,float(self.vnos_zneska.get())) == 1:
			return self.izhodni_podatki.set('Transakcija uspesno potekla!')
		elif self.racun.nakazi(self.okno_nakazilo.get() ,float(self.vnos_zneska.get())) == 0:
			return self.izhodni_podatki.set('Stanje na vasem racunu je prenizko')
		else:
			return self.izhodni_podatki.set('Transakcijska stevilka ne obstaja')



	def izhod(self):
		self.okno_nakazilo.delete(0, 'end') #problem, ker mi ne pocisti okna ob izpisu...
		self.glavno_okno.pack_forget()
		self.prijava.pack()

okno = Tk()
app = Bankomat_vmesnik(okno)
okno.mainloop()
