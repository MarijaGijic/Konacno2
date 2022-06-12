# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 10:47:43 2022

@author: Marija Gijic
"""
import pickle
from datetime import datetime
from Gradjanin import Osoba
from Gradjanin import Gradjanin
from Gradjanin import ZdravstveniRadnik
from Vakcina import Vakcina
from Doza import Doza
from PotvrdaOIzvrsenojVakcinaciji import PotvrdaOIzvrsenojVakcinaciji
from DigitalniSertifikat import DigitalniSertifikat

class Podaci:
    
    @property 
    def lista_gradjana(self):
        return self.__lista_gradjana   
   
    @property 
    def zdravstveni_radnici(self):
        return self.__zdravstveni_radnici
    @property 
    def doze(self):
        return self.__doze
    @property 
    def potvrde(self):
        return self.__potvrde
    @property 
    def digitalni_sertifikati(self):
        return self.__digitalni_sertifikati
   
    def __init__(self):
        self.__lista_gradjana = []
        self.__zdravstveni_radnici = []
        self.__doze = []
        self.__potvrde = []
        self.__digitalni_sertifikati = []
        
    
        
    @classmethod 
    def napravi_pocetne(cls):
        podaci = Podaci()
        lista_gradjana = podaci.lista_gradjana
        lista_gradjana.append(Gradjanin("121213121", "Marko", "Matic", "3-3-2002", "m", "13124232424"))
        lista_gradjana.append(Gradjanin("1212323221", "Ana", "Miric", "2-3-2000", "z", "132131231123"))
        lista_gradjana.append(Gradjanin("13211312321", "Slavko", "Suzic", "3-12-2001", "m", "21224232424"))
        zdravstveni_radnici = podaci.zdravstveni_radnici
        zdravstveni_radnici.append(ZdravstveniRadnik("12313132", "Mirko", "Savic", "2-2-1998", "m", "Bolnica"))
        
        doza1 = lista_gradjana[0]
        doza1.dodaj_primljene_doze(Doza("12-2-2021", Vakcina("Fajzer", "123123", "Nemacka", "12-2-2022"),
                                        zdravstveni_radnici[0].ime,"US", lista_gradjana[0].ime))
        doza1.dodaj_primljene_doze(Doza("12-2-2022", Vakcina("Astra zeneka", "111111", "Amerika", "12-2-2023"),
                                        zdravstveni_radnici[0].ime,"US", lista_gradjana[0].ime))
        
        doza2 = lista_gradjana[1]
        doza2.dodaj_primljene_doze(Doza("2-2-2021", Vakcina("Fajzer", "123212", "Nemacka", "2-2-2023"),
                                        zdravstveni_radnici[0].ime,"US", lista_gradjana[1].ime))
        
        doza3 = lista_gradjana[2]
        doza3.dodaj_primljene_doze(Doza("3-3-2022", Vakcina("Fajzer", "123123", "Nemacka", "2-2-2024"),
                                        zdravstveni_radnici[0].ime,"US", lista_gradjana[2].ime))
        
        doze = podaci.doze
        doze.append(doza1.primljene_doze)
        doze.append(doza2.primljene_doze)
        doze.append(doza3.primljene_doze)
        
        potvrda1 = lista_gradjana[0]
        potvrda1.dodaj_potvrde_o_izvrsenoj_vakcinaciji(PotvrdaOIzvrsenojVakcinaciji("123213123", "12-2-2022", 
                                                                                    doze[0], lista_gradjana[0].ime, zdravstveni_radnici[0].ime))
        
        potvrda1.dodaj_potvrde_o_izvrsenoj_vakcinaciji(PotvrdaOIzvrsenojVakcinaciji("12322123", "12-2-2022", 
                                                                                    doze[0], lista_gradjana[0].ime, zdravstveni_radnici[0].ime))
       
        potvrda2 = lista_gradjana[1]
        potvrda2.dodaj_potvrde_o_izvrsenoj_vakcinaciji(PotvrdaOIzvrsenojVakcinaciji("223213123", "12-2-2023", 
                                                                                    doze[1], lista_gradjana[1].ime, zdravstveni_radnici[0].ime))
        
        potvrda3 = lista_gradjana[2]
        potvrda3.dodaj_potvrde_o_izvrsenoj_vakcinaciji(PotvrdaOIzvrsenojVakcinaciji("553213123", "12-2-2021", 
                                                                                    doze[2], lista_gradjana[2].ime, zdravstveni_radnici[0].ime))
        
        potvrde = podaci.potvrde
        potvrde.append(potvrda1.potvrde_o_izvrsenoj_vakcinaciji)
        potvrde.append(potvrda2.potvrde_o_izvrsenoj_vakcinaciji)
        potvrde.append(potvrda3.potvrde_o_izvrsenoj_vakcinaciji)
        
        
        digitalni_sertifikati = podaci.digitalni_sertifikati
        
        sertifikat1 = lista_gradjana[0]
        sertifikat1.dodaj_digitalni_sertifikat(DigitalniSertifikat("123123123", "12-2-2021", lista_gradjana[0].ime))

        sertifikat2 = lista_gradjana[1]
        sertifikat2.dodaj_digitalni_sertifikat(DigitalniSertifikat("223333223", "2-2-2022", lista_gradjana[1].ime))    
        
        sertifikat3 = lista_gradjana[2]
        sertifikat3.dodaj_digitalni_sertifikat(DigitalniSertifikat("555565666", "2-2-2021", lista_gradjana[2].ime))
        
        
        digitalni_sertifikati.append(sertifikat1.digitalni_sertifikat)
        digitalni_sertifikati.append(sertifikat2.digitalni_sertifikat)
        digitalni_sertifikati.append(sertifikat3.digitalni_sertifikat)
        
        
        return podaci
    
 
    
    __datoteka = "podaci_gradjani.txt"
    
    @classmethod 
    def sacuvaj(cls, podaci):
        datoteka = open(cls.__datoteka, "wb")
        pickle.dump(podaci, datoteka)
        datoteka.close()
        
        
    @classmethod
    def ucitaj(cls):
        try:
            datoteka = open(cls.__datoteka, "rb")
            podaci = pickle.load(datoteka)
            datoteka.close()
        except FileNotFoundError:  
            return Podaci.napravi_pocetne()  

        return podaci
    
    
    def pronadji_gradjanina_po_jmbg(self,  jmbg):
        for gradjanin in self.__lista_gradjana:
            if gradjanin.jmbg == jmbg:
                return gradjanin

    def dodaj_gradjana(self, gradjanin):
        self.__lista_gradjana.append(gradjanin)

    def obrisi_gradjana(self, indeks):
        gradjanin = self.__lista_gradjana.pop(indeks)

        doze_za_brisanje = []
        potvrde_za_brisanje = []
        digitalni_sertifikat_za_brisanje = []
        for doza in self.__doze:
            if doza.sadrzi(gradjanin):
                doze_za_brisanje.append(doza)
        for doza in doze_za_brisanje:
            self.__doze.remove(doza)
                
        for potvrda in self.__potvrde:
            if potvrda.sadrzi(gradjanin):
                potvrde_za_brisanje.append(potvrda)
        
        for potvrda in potvrde_za_brisanje:
            self.__potvrde.remove(potvrda)
                
        for sertifikat in self.__digitalni_sertifikati:
            if sertifikat.sadrzi(gradjanin):
                digitalni_sertifikat_za_brisanje.append(sertifikat)
                
        for sertifikat in digitalni_sertifikat_za_brisanje:
            self.__digitalni_sertifikat.remove(sertifikat)


                

