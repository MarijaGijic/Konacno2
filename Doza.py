# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 21:08:30 2022

@author: Marija Gijic
"""
from datetime import datetime
from Gradjanin import Osoba
from Gradjanin import Gradjanin
from Gradjanin import ZdravstveniRadnik
from Vakcina import Vakcina

class Doza:
    @property
    def datum_vakcinacije(self):
        return self.__datum_vakcinacije
    @datum_vakcinacije.setter 
    def datum_vakcinacije(self, datum_vakcinacije):
        self.__datum_vakcinacije = datum_vakcinacije
        
    @property 
    def vakcina(self):
        return self.__vakcina
    @vakcina.setter
    def vakcina(self, vakcina):
        self.__vakcina = vakcina
        
    @property
    def zdravstveni_radnik(self):
        return self.__zdravstveni_radnik
    
    @property 
    def zemlja(self):
        return self.__zemlja
    @zemlja.setter 
    def zemlja(self, zemlja):
        self.__zemlja = zemlja
        
    @property
    def gradjanin(self):
        return self.__gradjanin
    
    
    def __init__(self, datum_vakcinacije, vakcina, zdravstveni_radnik, zemlja, gradjanin):
        self.__datum_vakcinacije = datum_vakcinacije
        self.__vakcina = vakcina
        self.__zdravstveni_radnik = zdravstveni_radnik
        self.__zemlja = zemlja
        self.__gradjanin = gradjanin
    
    
    
    def __str__(self):
        format_linije = "{:>10}: {}"
        return "\n".join([
            "",
            format_linije.format("Datum vakcinacije",datetime.strptime(self.__datum_vakcinacije, "%d-%m-%Y").date()),
            format_linije.format("Vakcina", self.__vakcina.naziv),
            format_linije.format("Zdravstveni radnik", "{} {}".format(self.__zdravstveni_radnik.ime, self.__zdravstveni_radnik.prezime )),
            format_linije.format("Zemlja", self.__zemlja),
            format_linije.format("Gradjanin", "{} {}".format(self.__gradjanin.ime, self.__gradjanin.prezime))
            ])
        
    def sadrzi(self, gradjanin):
        return gradjanin in self.__gradjanin
    
print(Doza("12-2-2021", Vakcina("Fajzer", "1231231", "Nemacka", "12-2-2022"), 
           ZdravstveniRadnik("213123123", "Marko", "Mirkovic", "12-3-2003", "m", "nesto"),
           "Nemacka", Gradjanin("1223232332", "Maria", "cscsc", "2-2-2003", "m", "123123123123")))    
