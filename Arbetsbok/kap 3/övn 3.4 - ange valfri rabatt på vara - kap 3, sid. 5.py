#!/usr/local/bin/python3.9

# Filnamn: övn 3.4 - ange valfri rabatt på vara - kap 3, sid. 5.py

# Skapa program eller skript
# Programmeringsövningar till kapitel 3 - Arbetsbok

# Programmet frågar först efter ordinarie pris på en vara. Därefter frågar det
# efter en godtycklig rabattprocent
# Till sist skriver det ut ett extrapris som ger den inmatade rabatten på
# ordinariepris

# Skriv ut programmets rubrik
print('Extrapris')
print('=========\n')

# Fråga efter ordinarie pris och rabattprocent. Därefter omvandla siffrorna från sträng till decimaltal
ordinariePris = float(input('Ange ordinarie pris: '))
rabattProcent = float(input('Ange rabattprocenten: '))

decimalRabattProcent = rabattProcent / 100 # Omvandlar procenttalet till ett decimaltal för senare beräkning

# Beräkna extrapriset 100% - rabattProcent * ordinarie pris
extraPris = (1 - decimalRabattProcent)  * ordinariePris

# Skriv ut rabattprocenten med noll decimaler och extrapriset med två decimalers noggranhet
print('Extrapriset blir med {0:.0f} % rabatt: {1:.2f} kr.'.format(rabattProcent, extraPris))
