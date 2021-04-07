#!/usr/local/bin/python3.9

# Filnamn: kap. 10, sid. 124 - upprepa slumpade talföljden.py
# Kapitel 10 - Slumptal i programmering
# Programmering 1 med Python - Lärobok

# Import av moduler med extra funktioner 
from random import randrange  

# Programmet visar den relativa frekvensen för hur många gånger tärning med 
# ett öga uppkommit osv. på 1000 kast

# frekvenstabell med 7 element som motsvarar ögonen på en tärning
# Första elementet används inte
frekvens = [0, 0, 0, 0, 0, 0, 0]

# Kasta 1000 tärningar och lagra antalet 1, 2, 3, 4, 5, och 6 i frekvenslistan
for c in range(1,1001):
    frekvens[randrange(1,7)] += 1

# Skriv ut frekvenstabellen
for c in range(1,7):
    print('Relativa frekvensen för tärning med siffra {:d} = {:4.3f}'.format(c, frekvens[c]/1000))
