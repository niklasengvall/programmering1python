#!/usr/bin/python3

# Filnamn: övn 3.5 - beräkna bensinpris - kap 3, sid. 5.py

# Skapa program eller skript
# Programmeringsövningar till kapitel 3 - Arbetsbok

# Programmet frågar efter tankad volym i liter och efter bensinpris i kr/liter.
# Därefter skriver det ut ett kvitto.

# Skriv ut programmets rubrik
print('Beräkna bensinpris')
print('==================\n')

# Fråga efter tankad volym i liter och bensinpris i kr/liter
# och omvandla siffrorna från sträng till decimaltal
liter = float(input('Hur många liter tankade du? '))
bensinPris = float(input('Ange bensinpriset kr/liter: '))

# Beräkna vad kunden betalar
attBetala = bensinPris * liter

# Skriv ut ett kvitto
print('+-----------------------------------+')
print('|            KVITTO                 |')
print('|                                   |')
print('|   Tankad volym:   {:>7.0f} liter   |'.format(liter))
print('|   Pris per liter: {:>7.2f} kr      |'.format(bensinPris))
print('|   Betalt:         {:>7.2f} kr      |'.format(attBetala))
print('|                                   |')
print('|   Tack för besöket och            |')
print('|   välkommen åter!                 |')
print('+-----------------------------------+')
