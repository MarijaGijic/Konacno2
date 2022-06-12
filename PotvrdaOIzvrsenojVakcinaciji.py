# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 21:19:09 2022

@author: Marija Gijic
"""
from datetime import datetime
from Gradjanin import Osoba
from Gradjanin import Gradjanin
from Gradjanin import ZdravstveniRadnik
from Doza import Doza

class PotvrdaOIzvrsenojVakcinaciji:
    @property
    def sifra_potvrde(self):
        return self.__sifra_potvrde
    @property 
    def datum_izdavanja_potvrde(self):
        return self.__datum_izdavanja_potvrde
    @datum_izdavanja_potvrde.setter 
    def datum_izdavanja_potvrde(self, datum_izdavanja_potvrde):
        shortDate = datetime.today().strftime('%d-%m-%Y')
        if datum_izdavanja_potvrde > shortDate:
            print("Morate uneti najkasnije tekuci datum")
        self.__datum_izdavanja_potvrde = datum_izdavanja_potvrde
    
    @property
    def doza(self):
        return self.__doza
    @property 
    def gradjanin(self):
        return self.__gradjanin
    @property 
    def zdravstveni_radnik(self):
        return self.__zdravstveni_radnik
    
    def __init__(self, sifra_potvrde, datum_izdavanja, doza, gradjanin, zdravstveni_radnik):
        self.__sifra_potvrde = sifra_potvrde
        self.__datum_izdavanja = datum_izdavanja
        self.__doza = doza
        self.__gradjanin = gradjanin
        self.__zdravstveni_radnik = zdravstveni_radnik
    
    def __str__(self):
        format_linije = "{:>10}: {}"
        return "\n".join([
            "",
            format_linije.format("Sifra potvrde", self.__sifra_potvrde),
            format_linije.format("Datum izdavanja", datetime.strptime(self.__datum_izdavanja, "%Y-%m-%d").date()),
            format_linije.format("Doza", self.__doza.vakcina),
            format_linije.format("Gradjanin","{} {}".format(self.__gradjanin.ime, self.__gradjanin.prezime)),
            format_linije.format("Zdravstveni radnik","{} {}".format(self.__zdravstveni_radnik.ime, self.__zdravstveni_radnik.prezime))
            ])

    def sadrzi(self, gradjanin):
        return gradjanin in self.__gradjanin
    
    
    