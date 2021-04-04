#!/usr/local/bin/python3.9

# Filnamn: kap. 6, sid. 76 - kontrollera innehåll och tomma strängar.py

# Kapitel 6 - Mer om teckensträngar i Python
# Programmering 1 med Python - Lärobok

# Kontrollera innehåll i en sträng med operatorn in
if 'r' in 'Räven raskar över isen':    # Kontroll av enstaka tecken
    print('Bokstaven r finns!')
if 'rask' in 'Räven raskar över isen': # Kontroll av fras/ord/orddel
    print('Frasen/ordet eller orddelen finns!')

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