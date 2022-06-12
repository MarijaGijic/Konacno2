# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 21:14:44 2022

@author: Marija Gijic
"""
from datetime import datetime

class Vakcina:
    @property 
    def naziv(self):
        return self.__naziv #bar dva karaktera
    @naziv.setter 
    def naziv(self, naziv):
        self.__naziv = naziv
    @property 
    def serijski_broj(self):
        return self.__serijski_broj #10 karaktera, jedinstven
    @serijski_broj.setter 
    def serijski_broj(self, serijski_broj):
        self.__serijski_broj = serijski_broj
        
    @property
    def zemlja_porekla(self):
        return self.__zemlja_porekla #bar dva karaktera
    @zemlja_porekla.setter 
    def zemlja_porekla(self, zemlja_porekla):
        self.__zemlja_porekla = zemlja_porekla
    @property
    def rok_trajanja(self):
        return self.__rok_trajanja
    
    def __init__(self, naziv, serijski_broj, zemlja_porekla, rok_trajanja):
        self.__naziv = naziv
        self.__serijski_broj = serijski_broj
        self.__zemlja_porekla = zemlja_porekla
        self.__rok_trajanja = rok_trajanja
    
    def __str__(self):
        format_linije = "{:>10}: {}"
        return "\n".join([
            "",
            format_linije.format("Naziv", self.__naziv),
            format_linije.format("Serijski broj", self.__serijski_broj),
            format_linije.format("Zemlja porekla", self.__zemlja_porekla),
            format_linije.format("Rok trajanja", datetime.strptime(self.__rok_trajanja, "%d-%m-%Y").date())
            ])