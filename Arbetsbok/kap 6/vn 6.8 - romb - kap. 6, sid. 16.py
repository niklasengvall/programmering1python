#!/usr/bin/python3.8

# Filnamn: övn 6.8 - romb - kap. 6, sid. 16.py

# Mer om teckensträngar i Python
# Programmeringsövningar till kapitel 6

# Programmet använder metoden .center samt operatorn * för att skapa en snygg 
# romb med asterisker

# Skriv ut den övre delen av romben
for antStjärnor in range(1, 30, 2):
    rad = (antStjärnor * '*').center(29, ' ')
    print(rad)

# Skriv ut den nedre delen av romben
for antStjärnor in range(27, 0, -2):
    rad = (antStjärnor * '*').center(29, ' ')
    print(rad)    