#!/usr/local/bin/python3.9

# Filnamn: kap. 16, sid. 182 - lista till sträng.py

# Kapitel 16 - Mer om listor samt dictionaries
# Programmering 1 med Python - Lärobok

# Kodexempel från boken med förklaringar

# För att omvandla en lista till sträng använder man strängmetoden .join
lista = ['K','a','l','l','e']
namnMedSpace = ' '.join(lista)
namn = ''.join(lista)
print('Lista:', lista)
print('Omvandlad till sträng med extra luft:', namnMedSpace)
print('Omvandlad till sträng:', namn)
