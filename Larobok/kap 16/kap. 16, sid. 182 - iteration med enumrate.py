#!/usr/local/bin/python3.7

# Filnamn: kap. 16, sid. 182 - iteration med enumrate.py

# Kapitel 16 - Mer om listor samt dictionaries
# Programmering 1 med Python - Lärobok

# Kodexempel från boken med förklaringar

# För att få index och listelement samtidigt använder man funktionen enumerate()
# Det är en snabbare metod än att använda den gamla klassiska metoden
print('Med enumerate()')
namn = "Agnes"
for i, bokstav in enumerate(namn):
    print(i, '=', bokstav, end = ', ')

print()
# Gammal metod med for-loop
print('for-loop')
namn = "Agnes"
for i in range(len(namn)):
    print(i, '=', namn[i], end = ', ')

print()
# Gammal metod med while-loop
print('while-loop')
namn = "Agnes"
i = 0
while i < len(namn):
    print(i, '=', namn[i], end = ', ')
    i += 1

print()
# Enumrate() med listor
print('Med enumerate() och vanliga listor')
skala = [-40, -30, -20, -10, 0, 10, 20, 30, 40, 50]
for i, element in enumerate(skala):
    print(i, '=', element, end=', ')
    

