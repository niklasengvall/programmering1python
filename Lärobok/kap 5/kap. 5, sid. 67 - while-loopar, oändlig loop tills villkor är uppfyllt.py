#!/usr/local/bin/python3.9

# Filnamn: kap. 5, sid. 67 - while-loopar, oändlig loop tills villkor är 
# uppfyllt.py

# Kapitel 5 - Loopar - upprepning, itteration
# Programmering 1 med Python - Lärobok

# Programmet repeterar en fråga om man vill fortsätta tills man svarar n eller N

print('Är du trött på Python, eller?')

while True:
    answer = input('Svara (J/N)? ')
    if answer == 'N' or answer == 'n':
        # Avbryt while-loopen 
        break

print('Tänkte väl det, men ta en paus nu!')