#!/usr/bin/python3.8

# Filnamn: kap. 5, sid. 66 - while-loopar, exempel 3.py

# Kapitel 5 - Loopar - upprepning, itteration
# Programmering 1 med Python - Lärobok

# Programmet skriver ut talen 20 - 40
# och deras kvadrater. Vi använder 
# styrkoden \t för att få utskriften i kolumner

print('Kvadreringstabell')
print('=================')
print('Tal\tKvadrat')

k = 20
while k <= 40:
    print(k, '\t', k*k)  
    k += 1