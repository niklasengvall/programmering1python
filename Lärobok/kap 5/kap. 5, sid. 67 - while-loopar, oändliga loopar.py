#!/usr/local/bin/python3.9

# Filnamn: kap. 5, sid. 67 - while-loopar, oändliga loopar.py

# Kapitel 5 - Loopar - upprepning, itteration
# Programmering 1 med Python - Lärobok

# Programmet räknar upp siffror på skärmen i det oändliga, tills användaren
# avbryter exekveringen med tangentkombinationen Ctrl+C

c = 1
while True:
    print(c, end = ' ')
    c += 1