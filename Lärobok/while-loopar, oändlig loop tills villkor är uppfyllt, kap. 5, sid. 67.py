#!/usr/bin/python3

# Filnamn: while-loopar, oändlig loop tills villkor är uppfyllt, kap. 5, 
# sid. 67.py

# Programmet repeterar en fråga om man vill fortsätta tills man svarar n eller N

print('Detta är ett skojigt program')

while True:
    svar = input('Vill du fortsätta (J/N)? ')
    if svar == 'N' or svar == 'n':
        break                                   # Avbryt loopen 

print('OK då. Tack för idag!')