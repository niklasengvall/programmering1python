#!/usr/local/bin/python3.9

# Filnamn: övn 5.13 - fråga efter ord eller mening, kap. 5, sid. 10.py

# Programmet frågar efter ett ord eller en mening och skriver sedan ut det med
# mellanrum mellan varje bokstav.


mening = input('Ange ett ord eller en hel mening: ')

for tecken in mening:
    print(tecken, end = ' ')

print('')