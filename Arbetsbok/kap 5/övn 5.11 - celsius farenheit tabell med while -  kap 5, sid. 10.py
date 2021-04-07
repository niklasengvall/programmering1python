#!/usr/local/bin/python3.9

# Filnamn: övn 5.11 - celcius farenheit tabell med while - kap 5, sid. 10.py

# Loopar - upprepning, iteration
# Programmeringsövningar till kapitel 5 - Arbetsbok

# Programmet skriver ut en tabell med grader i celsius och dess motsvarighet i 
# farenheit. Tabellen visar från +40 ner till -40 grader celsius.
# I det här exemplet använder jag while-loopen

# Skriv ut rubrik
print('Celsius -> Farenheit')
print('====================')

# Deklarera och initiera variablerna
celsius = 40
farenheit = 0

# Visa gradantal från +40 till -40
while celsius > -41:
    farenheit = 32 + celsius * 9 / 5
    print('{0:>4d} C -> {1:>5.1f} F'.format(celsius, farenheit))
    celsius -= 1

input('\nTryck på en tangent...\n')