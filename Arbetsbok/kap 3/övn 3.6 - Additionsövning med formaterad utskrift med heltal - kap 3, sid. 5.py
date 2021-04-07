#!/usr/local/bin/python3.9

# Filnamn: övn 3.6 - Additionsövning med formaterad utskrift med heltal - kap 3
# sid. 5.py

# Skapa program eller skript
# Programmeringsövningar till kapitel 3 - Arbetsbok

# Additionsövning med formaterad utskrift
# Programmet skriver ut tal i en snygg additionsuppställning

# Skriv ut programmets rubrik
print('Enkel addition med tre siffror')
print('==============================\n')

# Deklaration och initiering av 3 tal
tal1 = 27
tal2 = 8
tal3 = 213

# Beräkna summan av de tre talen
summa = tal1 + tal2 + tal3

# Skriv ut en enkel additionsuppställning med formatering
print('{:>5}'.format(tal1))
print('{:>5}'.format(tal2))
print('+{:>4}'.format(tal3))
print('=====')
print('{:>5}'.format(summa))
