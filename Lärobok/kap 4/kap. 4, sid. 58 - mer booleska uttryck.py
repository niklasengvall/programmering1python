#!/usr/local/bin/python3.9

# Filnamn: kap. 4, sid. 58 - mer booleska uttryck.py

# Kapitel 4 - Villkor, IF-satser
# Programmering 1 med Python - Lärobok

# exempel på booleska operatorer
m = int(input('Ange månadens nummer: '))

# olika sätt för att kontrollera angivet månadsnummer
if m < 1 or m > 12:
    print('Fel: Ange korrekt månadsnummer mellan 1-12!')
else:
    print('Ok')
        
if m >= 1 and m <= 12:
    print('Ok')
else:
    print('Fel: Ange korrekt månadsnummer mellan 1-12!')
