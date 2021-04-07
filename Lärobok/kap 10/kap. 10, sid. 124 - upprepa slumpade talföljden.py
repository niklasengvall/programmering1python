#!/usr/local/bin/python3.9

# Filnamn: kap. 10, sid. 124 - upprepa slumpade talföljden.py
# Kapitel 10 - Slumptal i programmering
# Programmering 1 med Python - Lärobok

# Import av moduler med extra funktioner 
from random import getstate, setstate, randrange  

# Programmet visar hur man kan upprepa/komma ihåg slumptal genom att spara fröet

# Avläs slumptalsgeneratorns tillstånd och spara dess frö
frö = getstate()

# Slumpa 20 tal melan 1 och 100
for c in range(1,21):
    print(str(randrange(1,101)).rjust(4), end='')

print('\n\n')

# Återställ till startfröet
setstate(frö)

# Kör samma slump somm nyss, resultatet ska bli det samma som innan
for c in range(1,21):
    print(str(randrange(1,101)).rjust(4), end='')
