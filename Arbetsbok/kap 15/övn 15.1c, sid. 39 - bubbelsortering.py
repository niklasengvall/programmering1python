#!/usr/local/bin/python3.9

# Filnamn: övn 15.1c, sid. 39 - bubbelsortering.py

# Sortering
# Programmeringsövningar till kapitel 15

# Programmet utför bubbelsortering och avbryter om inga tal bytt plats under 
# ett pass, varje pass blir också kortare 

# Import av modul
from random import randint
from time import perf_counter

# Funktionsdefinitioner
def bubbelsortering(lista):
    index = 0
    byttPlats = False
    maxPass = len(lista) - 1
    antalPass = 0
    while antalPass <= maxPass:
        if lista[index] > lista[index + 1]:
            lista[index], lista[index + 1] = lista[index + 1], lista[index]
            byttPlats = True  
        index += 1
        # Hoppas över de redan sorterade talen i slutet av vektorn
        if index >= maxPass - antalPass:
            if byttPlats == False:
                break
            else:
                index = 0
                byttPlats = False
                antalPass += 1
# Huvudprogram
def main():
    antal = int(input('Hur många tal vill du sortera? '))

    # Sortera en lista med antal tal som är slumpade mellan 0 och 4 294 967 292 
    lista = [randint(0, 4294967292) for i in range(antal)]
    start = perf_counter()
    bubbelsortering(lista)
    end = perf_counter()
    print('Att sortera {:d} heltal tog {:f} sekunder med egen bubbelsorteringsfunktion'.format(antal, end - start))

    # Sortera med Pythons inbyggda funktion
    lista = [randint(0,4294967292) for i in range(antal)]
    start = perf_counter()
    # Sortera listan på plats
    lista.sort()
    end = perf_counter()
    print('Att sortera {:d} heltal tog {:f} sekunder med inbyggd sorteringsfunktion'.format(antal, end - start))

# Huvudprogram anropas 
main()