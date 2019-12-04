#!/usr/bin/python3.8

# Filnamn: kap. 9, sid. 114 - specifierad import av moduler.py

# Kapitel 9 - Funktioner
# Programmering 1 med Python - Lärobok

# En modul är inget annat än en pythonfil med massor av färdigskrivna 
# funktioner och konstanter. Python installeras med väldigt många moduler och 
# skulle du behöva fler så kan du söka på nätet eller göra dem själv.

# För att använda funktioner i en modul så ska du använda nyckelordet import
from math import sqrt, sin, e   # Specificerad import av vissa funktioner
print(e)                        # möjliggör att du slipper skriva modulnamn.
print(sqrt(25))
print(sin(0.5))