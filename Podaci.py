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
    def vakcine(self):
        return self.__vakcine
    
    @property 
    def doze(self):
        return self.__doze
    @property 
    def doze1(self):
        return self.__doze1
    @property 
    def potvrde(self):
        return self.__potvrde
    @property 
    def potvrde1(self):
        return self.__potvrde1
    @property 
    def digitalni_sertifikati(self):
        return self.__digitalni_sertifikati
   
    def __init__(self):
        self.__lista_gradjana = []
        self.__zdravstveni_radnici = []
        self.__vakcine = []
        self.__doze = []
        self.__doze1 = []
        self.__potvrde = []
        self.__potvrde1 = []
        self.__digitalni_sertifikati = []
        
        
    
        
    @classmethod 
    def napravi_pocetne(cls):
        podaci = Podaci()
        lista_gradjana = podaci.lista_gradjana
        lista_gradjana.append(Gradjanin("1111111111111", "Marko", "Matic", "3-3-2002", "muski", "1111111111"))
        lista_gradjana.append(Gradjanin("2222222222222", "Ana", "Miric", "2-3-2000", "zenski", "2222222222"))
        lista_gradjana.append(Gradjanin("3333333333333", "Slavko", "Suzic", "3-12-2001", "muski", "3333333333"))
        
        zdravstveni_radnici = podaci.zdravstveni_radnici
        zdravstveni_radnici.append(ZdravstveniRadnik("4444444444444", "Mirko", "Savic", "2-2-1998", "muski", "Bolnica"))
        
        vakcine = podaci.vakcine
        vakcine.append(Vakcina("Fajzer", "1234567890", "Nemacka", "12-2-2022"))
        vakcine.append(Vakcina("Astra Zeneka", "1234567899", "Amerika", "2-2-2025"))
        vakcine.append(Vakcina("Kineska", "1234567898", "Kina","5-5-2026"))
        vakcine.append(Vakcina("Sputni V", "1234567897", "Rusija", "4-3-2027"))
        
        doza1 = lista_gradjana[0]
        doza1.dodaj_primljene_doze(Doza("12-2-2021", vakcine[0],
                                        "{} {}".format(zdravstveni_radnici[0].ime,zdravstveni_radnici[0].prezime),
                                        "US","{} {}".format(lista_gradjana[0].ime, lista_gradjana[0].prezime)))
        
        doza1.dodaj_primljene_doze(Doza("5-2-2021", vakcine[1],
                                        "{} {}".format(zdravstveni_radnici[0].ime,zdravstveni_radnici[0].prezime),
                                        "UK","{} {}".format(lista_gradjana[0].ime, lista_gradjana[0].prezime)))
       
        
        
        
        doza2 = lista_gradjana[1]
        doza2.dodaj_primljene_doze(Doza("7-7-2021", vakcine[3],
                                        "{} {}".format(zdravstveni_radnici[0].ime,zdravstveni_radnici[0].prezime),
                                        "UK","{} {}".format(lista_gradjana[1].ime, lista_gradjana[1].prezime)))
        
        doza3 = lista_gradjana[2]
        doza3.dodaj_primljene_doze(Doza("6-2-2022", vakcine[2],
                                        "{} {}".format(zdravstveni_radnici[0].ime,zdravstveni_radnici[0].prezime),
                                        "Kina","{} {}".format(lista_gradjana[2].ime, lista_gradjana[2].prezime)))
        
        doze = podaci.doze
        doze.append(doza1.primljene_doze)
        doze.append(doza2.primljene_doze)
        doze.append(doza3.primljene_doze)
        
        doze1 = podaci.doze1
        for doza12 in doze:
            for doza in doza12:
                doze1.append(doza)
        
        potvrda1 = lista_gradjana[0]
        potvrda1.dodaj_potvrde_o_izvrsenoj_vakcinaciji(PotvrdaOIzvrsenojVakcinaciji("12345678", "5-5-2021", 
                                                                                    doza1.primljene_doze[0], "{} {}".format(lista_gradjana[0].ime, lista_gradjana[0].prezime), 
                                                                                    "{} {}".format(zdravstveni_radnici[0].ime, zdravstveni_radnici[0].prezime)))
        
        potvrda1.dodaj_potvrde_o_izvrsenoj_vakcinaciji(PotvrdaOIzvrsenojVakcinaciji("12345789", "8-2-2021", 
                                                                                    doza1.primljene_doze[1], "{} {}".format(lista_gradjana[0].ime, lista_gradjana[0].prezime),
                                                                                    "{} {}".format(zdravstveni_radnici[0].ime, zdravstveni_radnici[0].prezime)))
       
        potvrda2 = lista_gradjana[1]
        potvrda2.dodaj_potvrde_o_izvrsenoj_vakcinaciji(PotvrdaOIzvrsenojVakcinaciji("22222222", "9-9-2021", 
                                                                                    doza2.primljene_doze[0], "{} {}".format(lista_gradjana[1].ime, lista_gradjana[1].prezime),
                                                                                    "{} {}".format(zdravstveni_radnici[0].ime, zdravstveni_radnici[0].prezime)))
        
        potvrda3 = lista_gradjana[2]
        potvrda3.dodaj_potvrde_o_izvrsenoj_vakcinaciji(PotvrdaOIzvrsenojVakcinaciji("55555555", "12-2-2021", 
                                                                                    doza3.primljene_doze[0], "{} {}".format(lista_gradjana[2].ime, lista_gradjana[2].prezime),
                                                                                    "{} {}".format(zdravstveni_radnici[0].ime, zdravstveni_radnici[0].prezime)))
        
        potvrde = podaci.potvrde
        potvrde.append(potvrda1.potvrde_o_izvrsenoj_vakcinaciji)
        potvrde.append(potvrda2.potvrde_o_izvrsenoj_vakcinaciji)
        potvrde.append(potvrda3.potvrde_o_izvrsenoj_vakcinaciji)
        
        potvrde1 = podaci.potvrde1
        for potvrda12 in potvrde:
            for potvrda in potvrda12:
                potvrde1.append(potvrda)
        
        digitalni_sertifikati = podaci.digitalni_sertifikati
        
        sertifikat1 = lista_gradjana[0]
        sertifikat1.dodaj_digitalni_sertifikat(DigitalniSertifikat("88888888", "12-2-2021", "{} {}".format(lista_gradjana[0].ime, lista_gradjana[0].prezime)))
        sertifikat2 = lista_gradjana[1]
        sertifikat2.dodaj_digitalni_sertifikat(DigitalniSertifikat("22222222", "2-2-2021", "{} {}".format(lista_gradjana[1].ime, lista_gradjana[1].prezime)))    
        
        sertifikat3 = lista_gradjana[2]
        sertifikat3.dodaj_digitalni_sertifikat(DigitalniSertifikat("66666666", "3-3-2021", "{} {}".format(lista_gradjana[2].ime, lista_gradjana[2].prezime)))
        
        
        digitalni_sertifikati.append(sertifikat1.digitalni_sertifikat)
        digitalni_sertifikati.append(sertifikat2.digitalni_sertifikat)
        digitalni_sertifikati.append(sertifikat3.digitalni_sertifikat)
        
        
        return podaci
    
 
    
    __datoteka = "podaci_gradjani8.txt"
    
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


                

