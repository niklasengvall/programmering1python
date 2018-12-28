#!/usr/bin/python3.7

# Filnamn: strängmetoder - kap. 6, sid. 81.py

# Programmering 1 med Python - Lärobok
# Kapitel 6 - Mer om teckensträngar i Python

# Strängmetoder
# Här nedan visas några av de metoder som finns för att kunna påverka strängar, 
# alla nås med så kallad punktnotation
namn = 'Karl Pettersson'
mening = 'en mening med ord.'
namn2 = 'pelle pettersson'
blankaTkn = '   några få ord   '
ersätta = 'alla känner apan men apan känner ingen'
print(namn)                     # Orginalsträngen
nyNamn = namn.center(20, '*')   # Centerar, 20 tkn bredd, använd * som utfyllnad
print(nyNamn)                 
antalR = namn.count('r')        # Räkna antal förekomster av tecknet r 
print(antalR)      
antalSS = namn.count('ss')      # Räkna antal förekomster av tecknen ss
print(antalSS)                  
nyNamn = namn.rjust(20)         # Högerjusterar, 20 tkn bredd
print(nyNamn)          
nyNamn = namn.rjust(20, '+')    # Högerjusterar, 20 tkn bredd, med utfyllnad
print(nyNamn)     
nyNamn = namn.ljust(20)         # Vänsterjusterar, 20 tkn bredd
print(nyNamn)          
nyNamn = namn.ljust(20, '+')    # Vänsterjusterar, 20 tkn bredd, med utfyllnad
print(nyNamn)     
nyNamn = namn.upper()           # Konverterar till VERSAL stil
print(nyNamn)     
nyNamn = namn.lower()           # Konverterar till gemen stil
print(nyNamn)     
nyMening = mening.capitalize()  # Gör stor första bokstav
print(nyMening)     
nyNamn2 = namn2.title()         # Gör stor bokstav i varje ord
print(nyNamn2)
oBlankaTkn = blankaTkn.strip()  # Ta bort mellanrum före och efter sträng
print(oBlankaTkn)
ersatt = ersätta.replace('apan','gorillan') # ersätt delsträng med annan sträng
print(ersatt)

