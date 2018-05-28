from tkinter import *
from Model_racun import *


class Bankomat_vmesnik():

	def __init__(self, okno):

		self.prijava = Frame(okno)

		self.obvestilo = Label(self.prijava, font = "Helvetica 20 bold", text='Pozdravljeni v Piton banki!')
		self.vpisi_pin = Label(self.prijava, font = "Helvetica 20" , text='Tukaj vpisite svojo PIN kodo:')
		self.vnos_pin = Entry(self.prijava, font = "Helvetica 20 bold", width=6, show='•', justify='center')
		self.potrdi_pin = Button(self.prijava, text='POTRDI', command=self.preveri_pin)


		self.glavno_okno = Frame(okno)

		self.vnos = Label(self.glavno_okno, text='Vnesi znesek:')
		self.vnos_zneska = Entry(self.glavno_okno, justify='center')
		self.nakazilo_na = Entry(self.glavno_okno, justify='center')
		self.polog = Button(self.glavno_okno, text='polog')
		self.dvig = Button(self.glavno_okno, text='dvig')
		self.stanje = Button(self.glavno_okno, text='preveri stanje', command=self.racun)
		self.transakcije = Button(self.glavno_okno, text='preveri transakcije')
		self.nakazilo = Button(self.glavno_okno, text='poslji nakazilo')
		self.izhod = Button(self.glavno_okno, text='odjava', command=self.izhod)

		self.obvestilo.pack()
		self.vpisi_pin.pack()
		self.vnos_pin.pack() 
		self.potrdi_pin.pack()
		self.prijava.pack()

		self.vnos.pack()
		self.vnos_zneska.pack()
		self.polog.pack()
		self.dvig.pack()
		self.stanje.pack()
		self.transakcije.pack()
		self.nakazilo.pack()
		self.nakazilo_na.pack()
		self.izhod.pack()

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
					self.racun = Racun(st_racuna) ### ne vem a morm dat self.racun al racun
				else:
					pass
			return self.vnos_pin.delete(0, 'end')

	def izhod(self):
		self.glavno_okno.pack_forget()
		self.prijava.pack()

okno = Tk()
app = Bankomat_vmesnik(okno)
okno.mainloop()
