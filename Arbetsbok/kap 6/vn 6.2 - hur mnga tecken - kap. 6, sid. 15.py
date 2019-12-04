#!/usr/bin/python3.8

# Filnamn: övn 6.2 - hur många tecken - kap. 6, sid. 15.py

# Mer om teckensträngar i Python
# Programmeringsövningar till kapitel 6

# Programmet ber användaren mata in en sträng för att sedan rapportera 
# hur många tecken den innehåller

sträng = input('Mata in en sträng: ')
längd =len(sträng)
print('Din inmatade sträng består av {0:d} tecken.'.format(längd))