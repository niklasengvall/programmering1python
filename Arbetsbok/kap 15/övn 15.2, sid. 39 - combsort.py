#!/usr/local/bin/python3.8

# Filnamn: övn 15.2, sid. 39 - combsort.py

# Sortering
# Programmeringsövningar till kapitel 15

# Programmet utför en förbättrad bubbelsortering, kallad combsort

# Import av modul
from random import randint
from time import perf_counter

# Funktionsdefinitioner
def combsort(lista):
    gap = len(lista)
    listansLängd = gap
    bytt = True
    while(gap > 1 or bytt == True):
        # justera gapet nedåt
        gap = int(gap / 1.3)
        if(gap < 1): gap = 1 # Får ej bli mindre än 1
        i = 0
        bytt = False
        # Kamma igenom listan
        while((i + gap) < listansLängd):
            if lista[i] > lista[i + gap]:
                lista[i], lista[i + gap] = lista[i + gap], lista[i]
                bytt = True # Flagga att ett byte skett
            i += 1

# Huvudprogram
def main():
    antal = int(input('Hur många tal vill du sortera? '))

    # Sortera en lista med antal tal som är slumpade mellan 0 och 4 294 967 292 
    lista = [randint(0, 4294967292) for i in range(antal)]
    #print("Före: ", lista)
    start = perf_counter()
    combsort(lista)
    end = perf_counter()
    #print("Efter: ", lista)
    print('Att sortera {:d} heltal tog {:f} sekunder med egen comsort-funktion'.format(antal, end - start))

    # Sortera med Pythons inbyggda funktion
    lista = [randint(0,4294967292) for i in range(antal)]
    start = perf_counter()
    # Sortera listan på plats
    lista.sort()
    end = perf_counter()
    print('Att sortera {:d} heltal tog {:f} sekunder med inbyggd sorteringsfunktion'.format(antal, end - start))

# Huvudprogram anropas 
main()