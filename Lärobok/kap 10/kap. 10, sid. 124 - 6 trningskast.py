#!/usr/bin/python3.8

# Filnamn: kap. 10, sid. 124 - 6 tärningskast.py
# Kapitel 10 - Slumptal i programmering
# Programmering 1 med Python - Lärobok

# Import av moduler med extra funktioner 
from random import * # Importerar modul med slumptalfunktioner

# Programmet gör 6 st tärningskast
for c in range(1,7): # Tärningskast
    tärning = randrange(1,7) 
    print('Tärning ' + str(c) + ' visar ' + str(tärning) + ' st prickar.')