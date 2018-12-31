#!/usr/bin/python3.7

# Filnamn: övn 6.7 - snygg tabell - kap. 6, sid. 15.py

# Mer om teckensträngar i Python
# Programmeringsövningar till kapitel 6

# Programmet använder metoden .rjust för att skriva ut en snygg tabell över de 
# första tjugo talen, dess kvadrater och kuber.

# Skriv ut rubrik
#      1234567890123456789
print('Tal   Kvadrat   Kub')
print('===================')
for tal in range(1, 21):
    t = str(tal).rjust(3,' ')
    t2 = str(tal * tal).rjust(3,' ')
    t3 = str(tal * tal * tal).rjust(4,' ')
    print(t + '     ' + t2 + '    ' + t3)