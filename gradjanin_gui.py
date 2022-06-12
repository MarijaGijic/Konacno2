# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 20:18:16 2022

@author: Marija Gijic
"""

from datetime import datetime
from Gradjanin import Osoba
from Gradjanin import Gradjanin
from Doza import Doza
from Vakcina import Vakcina
from PotvrdaOIzvrsenojVakcinaciji import PotvrdaOIzvrsenojVakcinaciji
from DigitalniSertifikat import DigitalniSertifikat
from Podaci import Podaci
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class GlavniProzor(Tk):
    
    def komanda_izlaz(self):
        odgovor = messagebox.askokcancel("Izlaz iz programa", "Da li ste sigurni da zelite da izadjete iz programa", icon="warning")
        if odgovor == True:
            self.destroy()
            
    def komanda_o_aplikaciji(self):
        messagebox.showinfo("O aplikaciji", "Aplikacija je kreirana za potrebe projekta")
        
    def popuni_gradjani_listbox(self, lista_gradjana):
        self.__gradjani_listbox.delete(0, END)  # obrisati sve unose iz Listbox-a
        for gradjanin in lista_gradjana:  
            self.__gradjani_listbox.insert(END, "{} {}".format(gradjanin.ime, gradjanin.prezime))
            # napravi jedan unos u listi

        self.ocisti_labele()
        
    def popuni_labele(self, gradjanin):
        self.__vrednost_jmbg_labela["text"] = gradjanin.jmbg
        self.__vrednost_datum_rodjenja_labela["text"] = gradjanin.datum_rodjenja 
        self.__vrednost_pol_labela["text"] = gradjanin.pol
        self.__vrednost_broj_licne_karte_labela["text"] = gradjanin.broj_licne_karte
      #  self.__vrednost_digitalni_sertifikat_labela["text"] = gradjanin.digitalni_sertifikat
        
    def popuni_digitalni_sertifikat_labela(self, gradjanin):
        
        for sertifikat in gradjanin.digitalni_sertifikat:
            self.__vrednost_digitalni_sertifikat_labela["text"] = sertifikat.sifra_sertifikata
    
    def ocisti_labele(self):
        self.__vrednost_jmbg_labela["text"] = ""
        self.__vrednost_datum_rodjenja_labela["text"] = ""
        self.__vrednost_pol_labela["text"] = ""
        self.__vrednost_broj_licne_karte_labela["text"] = ""
        self.__vrednost_digitalni_sertifikat_labela["text"] = ""
        
    def ocisti_doze_listbox(self):
        self.__lista_primljenih_doza_listbox.delete(0,END)
    def ocisti_potvrde_listbox(self):
        self.__lista_potvrda_listbox.delete(0,END)
        
    def popuni_listu_doza(self, gradjanin):
        self.ocisti_doze_listbox()
        for doza in gradjanin.primljene_doze:
            self.__lista_primljenih_doza_listbox.insert(END,"{}".format(doza.vakcina.naziv))
               
       
    def popuni_listu_potvrda(self, gradjanin):
        self.ocisti_potvrde_listbox()
        for potvrda in gradjanin.potvrde_o_izvrsenoj_vakcinaciji:
            self.__lista_potvrda_listbox.insert(END, "{}".format(potvrda.sifra_potvrde))
        
        
        
    
    
    def promena_selekcije_u_listbox(self, event=None):
        if not self.__gradjani_listbox.curselection():
            self.ocisti_labele()
            self.__obrisi_button['state'] = DISABLED           
            self.__izmeni_button['state'] = DISABLED
            
            return
        
        indeks = self.__gradjani_listbox.curselection()[0]
        gradjanin = self.__podaci.lista_gradjana[indeks]
        self.popuni_labele(gradjanin)
        self.popuni_digitalni_sertifikat_labela(gradjanin)
        
        self.popuni_listu_doza(gradjanin)
        self.popuni_listu_potvrda(gradjanin)
            
        
       
        self.__obrisi_button['state'] = NORMAL
        self.__izmeni_button['state'] = NORMAL
               
       
    def komanda_ocisti(self):
        self.__gradjani_listbox.selection_clear(0, END) 
        self.promena_selekcije_u_listbox()

    def komanda_dodaj(self):
        dodavanje_gradjanina_prozor = DodavanjeGradjaninaProzor(self, self.__podaci)
        
        self.wait_window(dodavanje_gradjanina_prozor)  
        if dodavanje_gradjanina_prozor.otkazano:  
            return

        gradjanin = self.__podaci.lista_gradjana[0] 

        self.__gradjani_listbox.selection_clear(0, END) 
        self.__gradjani_listbox.insert(END, "{}: {}".format(gradjanin.ime, gradjanin.prezime))  
        self.__gradjani_listbox.selection_set(END)  
        self.promena_selekcije_u_listbox() 

    def komanda_obrisi(self):
        if messagebox.askquestion("Upozorenje", "Da li ste sigurni?", icon="warning") == "no":
            return

        
        indeks = self.__gradjani_listbox.curselection()[0]
        gradjanin = self.__podaci.lista_gradjana.pop(indeks)
    
        self.update()
      

        self.__gradjani_listbox.delete(indeks)  
        self.__gradjani_listbox.selection_set(indeks)  
        self.promena_selekcije_u_listbox() 

    def komanda_izmeni(self):
       
        indeks = self.__gradjani_listbox.curselection()[0]
        gradjanin = self.__podaci.lista_gradjana[indeks]

        izmena_gradjanina_prozor = IzmenaGradjaninaProzor(self, self.__podaci, gradjanin)  
        self.wait_window(izmena_gradjana_prozor)
        if izmena_gradjana_prozor.otkazano:
            return

        self.__gradjani_listbox.delete(indeks)  
        self.__gradjani_listbox.insert(indeks, "{}: {}".format(gradjanin.ime, gradjanin.prezime))  
        self.__gradjani_listbox.selection_set(indeks)  
        self.promena_selekcije_u_listbox()  
    
    def __init__(self, podaci):
        super().__init__()
        self.__podaci = podaci
        self.title("Aplikacija")
        self.minsize(700,700)
        
        menubar = Menu(self)
        
        self.config(menu=menubar)
        file_menu = Menu(menubar)
        file_menu.add_command(
            label='Exit',
            command=self.komanda_izlaz
            )
        menubar.add_cascade(
            label="File",
            menu=file_menu,
            underline=0
            )

        self.__prozori_menu = Menu(menubar, tearoff=0)
        self.__prozori_menu.add_command(
            label="Prozor sa gradjanima",
            command=self.komanda_izlaz
            )
        self.__prozori_menu.add_command(
            label="Prozor sa zdravstvenim radnicima",
            command=self.komanda_izlaz
            )
        self.__prozori_menu.add_command(
            label="Prozor sa vakcinama",
            command=self.komanda_izlaz
            )
        self.__prozori_menu.add_command(
            label="Prozor sa potvrdama",
            command=self.komanda_izlaz
            )
        self.__prozori_menu.add_command(
            label="Prozor sa digitalnim sertifikatima",
            command=self.komanda_izlaz
             )
        menubar.add_cascade(
            label = "Prozori",
            menu = self.__prozori_menu
            )
        
        pomoc_menu = Menu(menubar, tearoff=0)
        pomoc_menu.add_command(label="O aplikaciji", command=self.komanda_o_aplikaciji)
        menubar.add_cascade(label="Pomoc", menu=pomoc_menu)

    
        self.protocol("WM_DELETE_WINDOW", self.komanda_izlaz)
        
        self.__pretraga_labela = Label(self, text='Pretraga')
        self.__pretraga_labela.grid(row=0, column=0)
        input_pretraga = StringVar()
        self.__pretraga_entry = Entry(self, textvariable=input_pretraga)
        self.__pretraga_entry.grid(row=0, column=1)
        
        #listbox i scrollbar
        
        self.__gradjani_listbox = Listbox(self, activestyle="none",width=30, height= 25)
        self.__gradjani_listbox.grid(row=1, column=1, rowspan=6, columnspan=3)
        self.__gradjani_scrollbar = Scrollbar(self)
        self.__gradjani_scrollbar.grid(row=2, column=4, rowspan=3, columnspan=3)
        self.__gradjani_listbox.configure(yscrollcommand=self.__gradjani_scrollbar.set)
        self.__gradjani_scrollbar.configure(command=self.__gradjani_listbox.yview)
        
        #labela jmbg
        
        jmbg_labela = Label(self, text = "Jmbg:")
        jmbg_labela.grid(row = 0, column = 7)
        self.__vrednost_jmbg_labela = Label(self, text="Select")
        self.__vrednost_jmbg_labela.grid(row=0, column = 8)
        
        #labela datum rodjenaja
        
        datum_rodjenja_labela = Label(self, text = "Datum rodjenja: ")
        datum_rodjenja_labela.grid(row = 1, column = 7)
        self.__vrednost_datum_rodjenja_labela  = Label(self, text = "Select")
        self.__vrednost_datum_rodjenja_labela.grid(row = 1, column = 8)
        
        #labela pol
        
        pol_labela = Label(self, text = "Pol: ")
        pol_labela.grid(row = 2, column = 7)
        self.__vrednost_pol_labela  = Label(self, text = "Select")
        self.__vrednost_pol_labela.grid(row = 2, column = 8)
        
        #labela broj licne karte
        
        broj_licne_karte_labela = Label(self, text="Broj licne karte: ")
        broj_licne_karte_labela.grid(row = 3, column=7)
        self.__vrednost_broj_licne_karte_labela  = Label(self, text = "Select")
        self.__vrednost_broj_licne_karte_labela.grid(row = 3, column = 8)
        
        #labela i lista primljenih doza
        
        lista_primljenih_doza_labela = Label(self, text = "Lista primljenih doza: ")
        lista_primljenih_doza_labela.grid(row=4, column = 7)
        self.__lista_primljenih_doza_listbox = Listbox(self, width=20, height=5)
        self.__lista_primljenih_doza_listbox.grid(row=4, column=8)
        
        #labela i lista potvrda
        
        lista_potvrda_labela = Label(self, text="Lista potvrda: ")
        lista_potvrda_labela.grid(row=5, column=7)
        self.__lista_potvrda_listbox = Listbox(self, width=20, height=5)
        self.__lista_potvrda_listbox.grid(row = 5, column=8)
        
        #labela i digitalni sertifikat
        
        digitalni_sertifikat_labela = Label(self, text="Digitalni sertifikat:")
        digitalni_sertifikat_labela.grid(row = 6, column = 7)
        self.__vrednost_digitalni_sertifikat_labela  = Label(self, text = "Select")
        self.__vrednost_digitalni_sertifikat_labela.grid(row = 6, column = 8)
        
        #buttons
        
        self.__ocisti_button = Button(self, text="Ocisti", height= 2, width = 10, command = self.komanda_ocisti)
        self.__ocisti_button.grid(row=6, column = 10, sticky=SE)
        self.__dodaj_button = Button(self, text="Dodaj", height= 2, width = 10, command = self.komanda_dodaj)
        self.__dodaj_button.grid(row=7, column=10, sticky=SE)
        self.__obrisi_button = Button(self, text="Obrisi", state=DISABLED, height= 2, width = 10, command = self.komanda_obrisi)
        self.__obrisi_button.grid(row=8, column=10, sticky=SE)
        self.__izmeni_button = Button(self, text="Izmeni", state=DISABLED, height= 2, width = 10, command = self.komanda_izmeni)
        self.__izmeni_button.grid(row=9, column=10, sticky=SE)
        
        self.popuni_gradjani_listbox(self.__podaci.lista_gradjana)
        self.focus_force()  # fokusiran nakon prikazivanja
        self.__gradjani_listbox.bind("<<ListboxSelect>>", self.promena_selekcije_u_listbox)
       