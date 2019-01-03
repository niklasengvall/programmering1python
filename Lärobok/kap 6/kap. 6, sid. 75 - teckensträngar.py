#!/usr/bin/python3

# Filnamn: kap. 6, sid. 75 - teckensträngar.py

# Kapitel 6 - Mer om teckensträngar i Python
# Programmering 1 med Python - Lärobok

# En strängkonstant även kallad literal som spänner över flera rader
# Initieras och avslutas med tre st """
print("""Här har vi en massa gojja 
som dräller över tre
rader""")

# Kommentarer kan spänna över flera rader med hjälp av 
'''
print("""De här raderna är bortkommenterade med hjälp av 
tre inledande och avslutande apostrofer""")
'''

'''
name är en strängvariabel
'Linnea' är en strängkonstant, literal
'''
name = 'Linnea'

print(name)

# För att nå enskilda tecken i strängar, använd indexeringsfunktionen, [...]
print(name[0])
print(name[1])
print(name[2])