#!/usr/bin/python3.7

# Filnamn: övn 13.3, sid. 32 - rekursiv multiplikation.py

# Rekursion- Funktioner som anropar sig själva
# Programmeringsövningar till kapitel 13

# Programmet multiplicerar två tal med hjälp av rekursiv addition

# Funktionsdefinitioner
def mul(a, b):
    if b == 1:
        return a
    else:
        return a + mul(a, b - 1) 

# Huvudprogram
def main():
    tal1 = int(input('Skriv in faktor 1: '))
    tal2 = int(input('Skriv in faktor 2: '))

    produkt = mul(tal1, tal2)
    print('Produkten av talen ' + str(tal1) + ' och ' + str(tal2) + ' blir ' + str(produkt))

## Huvudprogram anropas 
main()