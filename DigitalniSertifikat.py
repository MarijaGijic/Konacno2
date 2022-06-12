# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 10:44:17 2022

@author: Marija Gijic
"""
from datetime import datetime
from Gradjanin import Osoba
from Gradjanin import Gradjanin

class DigitalniSertifikat:
    @property 
    def sifra_sertifikata(self):
        return self.__sifra_sertifikata
    @sifra_sertifikata.setter 
    def sifra_sertifikata(self, sifra_sertifikata):
        self.__sifra_sertifikata = sifra_sertifikata
    @property 
    def datum_izdavanja_sertifikata(self):
        return self.__datum_izdavanja_sertifikata
    @datum_izdavanja_sertifikata.setter 
    def datum_izdavanja_sertifikata(self, datum_izdavanja_sertifikata):
        shortDate = datetime.today().strftime('%d-%m-%Y')
        if datum_izdavanja_sertifikata > shortDate:
            print("Morate uneti najkasnije tekuci datum")
        self.__datum_izdavanja_sertifikata = datum_izdavanja_sertifikata
        
    @property
    def gradjanin(self):
        return self.__gradjanin
    
    def __init__(self, sifra_sertifikata, datum_izdavanja_sertifikata, gradjanin):
        self.__sifra_sertifikata = sifra_sertifikata
        self.__datum_izdavanja_sertifikata = datum_izdavanja_sertifikata
        self.__gradjanin = gradjanin
    
    def __str__(self):
        return "\n".join ([
            "",
            "{:>10}: {}".format("Sifra seritifikata", self.__sifra_sertifikata),
            "{:>10}: {}".format("Datum izdavanja", datetime.strptime(self.__datum_izdavanja_sertifikata, "%d-%m-%Y").date()),
            "{:>1o}: {}".format("Gradjanin", "{} {}".format(self.__gradjanin.ime, self.__gradjanin.prezime))
            ])
    def sadrzi(self, gradjanin):
        return gradjanin in self.__gradjanin
    