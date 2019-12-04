#!/usr/bin/python3.7

# Filnamn: kap. 10, sid. 123 - 10 slumptal mellan 1 och 1000.py

# Kapitel 10 - Slumptal i programmering
# Programmering 1 med Python - Lärobok

# Import av moduler med extra funktioner 
import random # Importerar modul med slumptalfunktioner

# Programmet skapar 5 st slumptal mellan 1 och 100
for c in range(1,6):
    slumptal = random.randrange(1,101) 
    print('Tal ' + str(c) + ': ' + str(slumptal))