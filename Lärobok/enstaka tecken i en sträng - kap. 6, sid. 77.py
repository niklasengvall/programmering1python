#!/usr/bin/python3.7

# Filnamn: enstaka tecken i en sträng - kap. 6, sid. 77.py

# Programmering 1 med Python - Lärobok
# Kapitel 6 - Mer om teckensträngar i Python

'''
Man kan koma åt de enskilda tecknen i en sträng genom att ange index inom 
hakparanteser direkt efter variabelnamnet. T.ex. var[0] som tar fram det
första tecknet i strängkonstanten som finns lagrad i strängvariabeln var.
'''

# Följande program skriver ut bokstäverna från strängkonstanten 'Anna' på
# fyra olika sätt. Först mha av vanliga print-satser, därefter while, sedan for 
# med range och sist for med in
n = 'Anna'
# vanliga print-satser med index
print(n[0]) # A
print(n[1]) # n
print(n[2]) # n
print(n[3]) # a

# while-sats
i = 0
while i < len(n):   # len(n) returnerar antalet tecken som strängen n består av
    # Skriver ut tecken för tecken med mellanslag bakom
    print(n[i] + ' ', end = '')
    i += 1

print() # Skapa ett radmellanrum. OBS! Dubbla '' kan utelämnas

# for-sats med range
for i in range(len(n)):
    print(n[i] + ' ', end = '')

print() 

# for-sats med in
for tecken in n:
    print(tecken)
    