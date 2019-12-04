#!/usr/bin/python3.7

# Filnamn: övn 3.3 - extrapris - kap 3, sid. 5.py

# Skapa program eller skript
# Programmeringsövningar till kapitel 3 - Arbetsbok

# Programmet frågar efter ordinarie pris på en vara och därefter skriver det
# ut ett extrapris som ger 15 % rabatt på ordinariepris
# Skriv ut programmets rubrik
print('Extrapris')
print('=========\n')

# Fråga efter ordinarie pris och omvandla det från sträng till decimaltal
ordinariePris = float(input('Ange ordinarie pris: '))


# Beräkna extrapriset 100% - 15 % * ordinarie pris
extraPris = (1 - 0.15)  * ordinariePris

# Skriv ut extrapriset med två decimalers noggranhet
print('Extrapriset blir med 15 % rabatt: {:.2f} kr.'.format(extraPris))
