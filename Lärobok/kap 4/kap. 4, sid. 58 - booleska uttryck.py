#!/usr/local/bin/python3.9

# Filnamn: kap. 4, sid. 58 - booleska uttryck.py

# Kapitel 4 - Villkor, IF-satser
# Programmering 1 med Python - Lärobok

# Att kombinera olika villkor med and, or och not
x = 3
y = 12
z = False

if x > y:
    print(x > y)
if x < y:
    print(x < y)
if x < y and y < 13:
    print(x < y and y < 13)
if x == 3 or y == 12:
    print(x == 3 or y == 12)
if not z: # Kör nedanstående rad om inte z är True
    print(z)

