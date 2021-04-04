#!/usr/local/bin/python3.9

# Filnamn: kap. 6, sid. 77 - enstaka tecken i en sträng.py

# Kapitel 6 - Mer om teckensträngar i Python
# Programmering 1 med Python - Lärobok

'''
Man kan koma åt de enskilda tecknen i en sträng genom att ange index inom 
hakparanteser direkt efter variabelnamnet. T.ex. var[0] som tar fram det
första tecknet i strängkonstanten som finns lagrad i strängvariabeln var.
'''

# Följande program skriver ut bokstäverna från strängkonstanten 'Agnes' på
# fyra olika sätt. Först mha av vanliga print-satser, därefter while, sedan for 
# med range och sist for med in
s = 'Agnes'
# vanliga print-satser med index
print(s[0]) # A
print(s[1]) # g
print(s[2]) # n
print(s[3]) # e
print(s[4]) # s

# while-sats
i = 0
while i < len(s):   # len(n) returnerar antalet tecken som strängen n består av
    # Skriver ut tecken för tecken med mellanslag bakom
    print(s[i] + ' ', end = '')
    i += 1

print() # Skapa ett radmellanrum. OBS! Dubbla '' kan utelämnas

# for-sats med range
for i in range(len(s)):
    print(s[i] + ' ', end = '')

print() 

# for-sats med in
for char in s:
    print(char)
    