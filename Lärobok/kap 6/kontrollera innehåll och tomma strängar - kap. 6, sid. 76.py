#!/usr/bin/python3

# Filnamn: kontrollera innehåll och tomma strängar - kap. 6, sid. 76.py

# Programmering 1 med Python - Lärobok
# Kapitel 6 - Mer om teckensträngar i Python

# Kontrollera innehåll i en sträng med operatorn in
if 'o' in 'Hej hopp i lingonskogen':    # Kontroll av enstaka tecken
    print('Finns')
if 'skog' in 'Hej hopp i lingonskogen': # Kontroll av fras/ord
    print('Finns')

'''
Exempel på tom sträng
En tom sträng tolkas alltid som falsk (False) vid villkorstestning
och undertrycker alltid en radframmatning i print-satser
Övriga strängar tolkas som sanna (True)
'''
s = ''
if s:
    print('Strängen är inte tom')
else:
    print('Strängen är tom')

s = 'Nisse'
if s:
    print('Strängen är inte tom')
else:
    print('Strängen är tom')