#!/usr/bin/python3.8

# Filnamn: kap. 11, sid. 130 - resa undantag.py

# Kapitel 11 - Felhantering i Python - undantag eller "Exceptions"
# Programmering 1 med Python - Lärobok

# Fler undantag

x = 20
y = 2 # Vi tar bort en variabel för ett sk. NameError

try:
    z = x / y 
    # Vi kan resa undantag med flit
    raise ZeroDivisionError
except (ZeroDivisionError, NameError):
    print('Fel: Vid division.')
else:
    print('Resultatet av divisionen:', z)

print('Här fortsätter vi programmet')
