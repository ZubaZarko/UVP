from tkinter import *
import Model_racun


class Bankomat_vmesnik():

	def __init__(self,okno):
		self.prijava = Frame(okno)
		self.obvestilo = Label(self.prijava, text='Pozdravljeni v Piton banki!')
		self.vpisi_pin = Label(self.prijava, text='Tukaj vpisite svojo PIN kodo:')
		self.vnos_pin = Entry(self.prijava)
		self.potrdi_pin = Button(self.prijava, text='POTRDI', command=self.preveri_pin)
		self.obvestilo.pack()
		self.vpisi_pin.pack()
		self.vnos_pin.pack() 
		self.potrdi_pin.pack()
		self.prijava.pack()

	def preveri_pin(self):
		pin = int(self.vnos_pin.get())
		with open('Uporabniski_podatki') as usernames:
			for vrstica in vhodna:
				if int(vrstica[24:].strip) == pin:
					self.racun = vrstica[:22]
				else:
					self.racun = None

okno = Tk()
app = Bankomat_vmesnik(okno)
okno.mainloop()