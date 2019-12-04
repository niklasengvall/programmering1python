#!/usr/bin/python3.7

# Filnamn: kap. 9, sid. 114 - import av moduler.py

# Kapitel 9 - Funktioner
# Programmering 1 med Python - Lärobok

# En modul är inget annat än en pythonfil med massor av färdigskrivna 
# funktioner och konstanter. Python installeras med väldigt många moduler och 
# skulle du behöva fler så kan du söka på nätet eller göra dem själv.

# För att använda funktioner i en modul så ska du använda nyckelordet import
import math    # En modul med många matematiska funktioner och konstanter
print(math.e) # För att komma åt modulens funktioner/konstanter, ange 
               # modulnamn plus en punkt och därefter funktionen/konstanten
print(math.pow(2, 5)) # 2 upphöjt i 5
print(math.sin(math.pi/3))