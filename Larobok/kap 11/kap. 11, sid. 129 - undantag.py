#!/usr/bin/python3.8

# Filnamn: kap. 11, sid. 129 - undantag.py

# Kapitel 11 - Felhantering i Python - undantag eller "Exceptions"
# Programmering 1 med Python - Lärobok

# Det finns olika feltyper i Python och för att fånga upp de som inte är 
# logiska och genererar körfel i programmen. För att fånga upp dessa och inte 
# låta Python krascha eller avbrytas abrupt så används konstruktionen 
# try...except

x = 20
y = 0

try:
    z = x / y # Genererar ett division med noll fel
except ZeroDivisionError:
    print('Division med noll.')

print('Här fortsätter vi programmet')
