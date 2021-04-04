#!/usr/local/bin/python3.9

# Filnamn: kap. 13, sid. 160 - rekursion, beräkna fakultet.py

# Kapitel 13 - Rekursion - funktioner som anropar sig själva
# Programmering 1 med Python - Lärobok

# Kodexempel från boken med förklaringar

# Fakultet n! = n * (n-1)!
# 
# Exempel 6! = 6 * 5 * 4 * 3 * 2 * 1 = 720
#         4! = 4 * 3! 

# Import av matematik modul och funktionen factorial
from math import factorial

def myFactorial(x):
    if x <= 1:
        return 1
    return x * myFactorial(x - 1)

# Skriv ut resultatet efter körning med egen funktion
print('Tal'.rjust(6)+'Fakultet'.rjust(12))
for c in range(1, 13):
    print('{:>6d}{:>12d}'.format(c, myFactorial(c)))

print()

# Skriv ut resultatet efter körning med mattemodulens factorial funktion
print('Tal'.rjust(6)+'Fakultet'.rjust(12))
for c in range(1, 13):
    print('{:>6d}{:>12d}'.format(c, factorial(c)))

