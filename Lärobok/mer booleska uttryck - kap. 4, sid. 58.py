#!/usr/bin/python3

# Filnamn: mer booleska uttryck - kap. 4, sid. 58.py

# exempel på booleska operatorer

month = int(input('Ange månadsnummer: '))

# ett par olika sätt att kontrollera rimligt månadsnummer
if month < 1 or month > 12:
    print('Felaktig månadsangivelse!')
else:
    print('OK!')
        
if month >= 1 and month <= 12:
    print('OK!')
else:
    print('Felaktig månadsangivelse!')
