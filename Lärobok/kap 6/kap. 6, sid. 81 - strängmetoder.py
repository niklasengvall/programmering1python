#!/usr/bin/python3.7

# Filname: kap. 6, sid. 81 - strängmetoder.py

# Kapitel 6 - Mer om teckensträngar i Python
# Programmering 1 med Python - Lärobok

# Strängmetoder
# Här nedan visas några av de metoder som finns för att kunna påverka strängar, 
# alla nås med så kallad punktnotation
name = 'Tage Test'
mening = 'en mening med ord.'
name2 = 'test testsson'
blankaTkn = '   några få ord   '
ersätta = 'bor du här? det visste inte du efter minnesförlusten.'
print(name)                     # Orginalsträngen
new_name = name.center(20, '*') # Centerar, 20 tkn bredd, använd * som utfyllnad
print(new_name)                 
antalR = name.count('r')        # Räkna antal förekomster av tecknet r 
print(antalR)      
antalSS = name.count('ss')      # Räkna antal förekomster av tecknen ss
print(antalSS)                  
new_name = name.rjust(20)       # Högerjusterar, 20 tkn bredd
print(new_name)          
new_name = name.rjust(20, '+')  # Högerjusterar, 20 tkn bredd, med utfyllnad
print(new_name)     
new_name = name.ljust(20)       # Vänsterjusterar, 20 tkn bredd
print(new_name)          
new_name = name.ljust(20, '+')  # Vänsterjusterar, 20 tkn bredd, med utfyllnad
print(new_name)     
new_name = name.upper()          # Konverterar till VERSAL stil
print(new_name)     
new_name = name.lower()          # Konverterar till gemen stil
print(new_name)     
new_Mening = mening.capitalize() # Gör stor första bokstav
print(new_Mening)     
new_name2 = name2.title()       # Gör stor bokstav i varje ord
print(new_name2)
oBlankaTkn = blankaTkn.strip()  # Ta bort mellanrum före och efter sträng
print(oBlankaTkn)
ersatt = ersätta.replace('du','jag') # ersätt delsträng med annan sträng
print(ersatt)

