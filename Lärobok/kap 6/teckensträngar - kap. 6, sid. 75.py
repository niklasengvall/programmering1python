#!/usr/bin/python3

# Filnamn: teckensträngar - kap. 6, sid. 75.py

# Programmering 1 med Python - Lärobok
# Kapitel 6 - Mer om teckensträngar i Python

# En strängkonstant även kallad literal som spänner över flera rader
# Initieras och avslutas med tre st """
print("""Här har vi en text
som spänner över flera
rader""")

# Kommentarer kan spänna över flera rader med hjälp av 
'''
print("""De här raderna är bortkommenterade med hjälp av 
tre inledande och avslutande apostrofer""")
'''

'''
namn är en strängvariabel
'Kalle' är en strängkonstant, literal
'''
namn = 'Kalle'

a = 'Kalle'
print(a)

# För att nå enskilda tecken i strängar, använd indexeringsfunktionen, [...]
print(a[0])
print(a[1])
print(a[2])