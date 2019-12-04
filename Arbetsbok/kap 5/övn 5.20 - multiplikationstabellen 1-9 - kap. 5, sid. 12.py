#!/usr/bin/python3.8

# Filnamn: övn 5.20 - multiplikationstabellen 1-9 - kap. 5, sid. 12.py

# Loopar - upprepning, iteration
# Programmeringsövningar till kapitel 5 - Arbetsbok

# Programmet skriver ut en multiplikationstabell med produkter av de 9 första
# talen. Talen i sig är högerjusterade med 3 tecken i bredd och istället för 
# radslutstecken så skrivs ett blanktecken ut bakom resultatet av 
# multiplikationen

for y in range(1, 10):
    for x in range(1, 10):
        print('{0:>3d}'.format(y*x), end = ' ')
    print('')