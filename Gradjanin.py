# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 18:39:14 2022

@author: Marija Gijic
"""

from datetime import datetime


class Osoba:
    @property
    def jmbg(self):
        return self.__jmbg #mora da ima 13 karaktera, jedinstven
    @jmbg.setter 
    def jmbg(self, jmbg):
        if len(jmbg) != 13:
            raise ValueError("Jmbg mora imati 13 karaktera!")
        da_li_je_broj = True
        try:
            int(jmbg)
        except ValueError:
            da_li_je_broj = False
        if da_li_je_broj != True:
            raise ValueError("Jmbg ne sme sadrzati nista osim brojeva")
        
        self.__jmbg = jmbg
        
    @property
    def ime(self):
        return self.__ime  #tipa string, najmanje 2 karaktera
    @ime.setter
    def ime(self, ime):
        if len(ime) < 2:
            raise ValueError("Ime mora sadrzati bar dva karaktera")
        self.__ime = ime
  
    @property
    def prezime(self):
        return self.__prezime  #tipa string, najmanje 2 karaktera
    @prezime.setter 
    def prezime(self, prezime):
        if len(prezime) < 2:
            raise ValueError("Prezime mora sadrzati bar dva karaktera")
        self.__prezime = prezime
    
    
    
    @property 
    def datum_rodjenja(self):
        return self.__datum_rodjenja #tip date, najkasnije tekuci datum
    @datum_rodjenja.setter 
    def datum_rodjenja(self, datum_rodjenja):
        shortDate = datetime.today().strftime('%d-%m-%Y')
        if datum_rodjenja > shortDate:
            print("Morate uneti najkasnije tekuci datum")
        self.__datum_rodjenja = datum_rodjenja
   
    @property 
    def pol(self):
        return self.__pol #tipa string, muski/zenski
    @pol.setter
    def pol(self, pol):
        self.__pol = pol
        
        
    def __init__(self, jmbg, ime, prezime, datum_rodjenja, pol):
        self.__jmbg = jmbg
        self.__ime = ime
        self.__prezime = prezime
        self.__datum_rodjenja = datum_rodjenja
        self.__pol = pol
        
    def __str__(self):
        format_linije = "{:>10}: {}"
        return "\n".join([
            "",
            format_linije.format("Jmbg", self.__jmbg),
            format_linije.format("Ime", self.__ime),
            format_linije.format("Prezime", self.__prezime),
            format_linije.format("Datum rodjenja", datetime.strptime(self.__datum_rodjenja, "%d-%m-%Y").date()),
            format_linije.format("Pol", self.__pol)
    
            
            ])

class Gradjanin(Osoba):
    @property
    def broj_licne_karte(self):
        return self.__broj_licne_karte #10 karaktera, jedinstven
    @broj_licne_karte.setter 
    def broj_licne_karte(self, broj_licne_karte):
        if len(broj_licne_karte) != 10:
            raise ValueError("Broj licne karte mora sadrzati 10 karaktera")
            
        self.__broj_licne_karte = broj_licne_karte
    @property 
    def primljene_doze(self): #lista primljenih doza
        return self.__primljene_doze
    
    @property 
    def potvrde_o_izvrsenoj_vakcinaciji(self):
        return self.__potvrde_o_izvrsenoj_vakcinaciji #lista potvrda o izvrsenoj vakc.
    @property 
    def digitalni_sertifikat(self): 
        return self.__digitalni_sertifikat
    
    
    def __init__(self, jmbg, ime, prezime, datum_rodjenja, pol, broj_licne_karte):
        super().__init__(jmbg, ime, prezime, datum_rodjenja, pol)
        self.__broj_licne_karte = broj_licne_karte
        self.__digitalni_sertifikat = []
        self.__primljene_doze = []
        self.__potvrde_o_izvrsenoj_vakcinaciji = []
        
    
    
    def dodaj_primljene_doze(self, doza):
        self.__primljene_doze.append(doza)
    
    def dodaj_potvrde_o_izvrsenoj_vakcinaciji(self, potvrda_o_izvrsenoj_vakcinaciji):
        self.__potvrde_o_izvrsenoj_vakcinaciji.append(potvrda_o_izvrsenoj_vakcinaciji)
    
    
    def dodaj_digitalni_sertifikat(self, digitalni_sertifikat):
       self.__digitalni_sertifikat.append(digitalni_sertifikat)
        
    
    def __str__(self):
        format_linije = "{:>10}: {}"
        return "\n".join([
            "",
            super().__str__(),
            format_linije.format("Broj licne", self.__broj_licne_karte),
            format_linije.format("Primljene doze", self.__primljene_doze),
            format_linije.format("Potvrde o izvrsenoj vakcinaciji", self.__potvrde_o_izvrsenoj_vakcinaciji),
            format_linije.format("Digitalni sertifikat", self.__digitalni_sertifikat)
            ])
    
class ZdravstveniRadnik(Osoba):
    @property
    def zdravstvena_ustanova(self):
        return self.__zdravstvena_ustanova
    @zdravstvena_ustanova.setter 
    def zdravstvena_ustanova(self, zdravstvena_ustanova):
        self.__zdravstvena_ustanova = zdravstvena_ustanova
        
    def __init__(self, jmbg, ime, prezime, datum_rodjenja, pol, zdravstvena_ustanova):
        super().__init__(jmbg, ime, prezime, datum_rodjenja, pol)
        self.__zdravstvena_ustanova = zdravstvena_ustanova
        
    def __str__(self):
        format_linije = "{:>10}: {}"
        return "\n".join([
            "",
            super().__str__(),
            format_linije.format("Zdravstvena ustanova", self.__zdravstvena_ustanova)
            ])
    

gradjanin = Osoba("12313131313", "Maria", "dbcscbsk", "12-2-2003", "m")
gradjanin.datum_rodjenja = "12-2-2023"
print(gradjanin)
g = Gradjanin("1223232332", "Maria", "cscsc", "2-2-2003", "m", "123123123123")

g.dodaj_primljene_doze("doza2")
g.dodaj_digitalni_sertifikat("sert1")
g.dodaj_potvrde_o_izvrsenoj_vakcinaciji("potv")
print(g)

