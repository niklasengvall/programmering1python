#!/usr/bin/python3.8

# Filnamn: övn 3.7 - Additionsövning med formaterad utskrift med flyttal - kap 3
# sid. 6.py

# Skapa program eller skript
# Programmeringsövningar till kapitel 3 - Arbetsbok

# Additionsövning med formaterad utskrift
# Programmet skriver ut tal i en snygg additionsuppställning

# Skriv ut programmets rubrik
print('Enkel addition med tre siffror i decimalform')
print('============================================\n')

# Deklaration och initiering av 3 tal
tal1 = 123.45
tal2 = 6.7
tal3 = 89.01

# Beräkna summan av de tre talen
summa = tal1 + tal2 + tal3

# Skriv ut ett kvitto
print('{:>8.2f}'.format(tal1))
print('{:>8.2f}'.format(tal2))
print('+{:>7.2f}'.format(tal3))
print('========')
print('{:>8.2f}'.format(summa))
