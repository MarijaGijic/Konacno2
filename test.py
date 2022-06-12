# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 20:26:02 2022

@author: Marija Gijic
"""

from datetime import datetime

from Podaci import Podaci
from gradjanin_gui import *

def test():
    # print("Učitavanje...")
    podaci = Podaci.ucitaj()
    if len(podaci.lista_gradjana) == 0:
        # print("Kreirani su podaci")
        podaci =  Podaci.napravi_pocetne()
    
    print("Čuvanje...")
    Podaci.sacuvaj(podaci)
    
    root = GlavniProzor(podaci)
    root.mainloop()

    print()

if __name__ == "__main__":
    test()