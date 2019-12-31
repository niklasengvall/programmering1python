#!/usr/bin/python3.7

# Filnamn: kap. 15, sid. 168 - urvalssortering.py

# Kapitel 15 - Sorteringar
# Programmering 1 med Python - Lärobok

# Kodexempel från boken med förklaringar

from random import randint
from time import perf_counter

def urvalssortering(l):
    # Yttre loop går igenom hela listan - ett element
    for j in range(len(l) - 1):
        # Låt varje nytt element få vara det minsta talet
        mTal = l[j]
        # Sätt indexposition till det satta minsta talet
        idx = j
        # Inre loop utgår från yttre loops index j + 1 och går igenom alla 
        # element i listan
        for i in range(j + 1, len(l)):
            # Om vi påträffar ett listelement som är mindre än tidigare minsta 
            # tal, sätt det nya talet som minsta tal och ändra index till det
            if l[i] < mTal:
                mTal = l[i]
                idx = i
        # Byt plats mellan listans minsta tal som antingen satts i yttre loop 
        # eller hittats i inre loop
        # swap-satsen nedan körs i onödan om inget mindre tal hittats i inre
        # loopen, därav if-sats
        if idx != j:
            l[j], l[idx] = l[idx], l[j]
 
antal = int(input('Hur många tal vill du sortera? '))

# Sortera en lista med antal tal som är slumpade mellan 0 och 4 294 967 292 
lista = [randint(0, 4294967292) for i in range(antal)]
start = perf_counter()
urvalssortering(lista)
end = perf_counter()
print('Att sortera {:d} heltal tog {:f} sekunder med egen urvalssorteringsfunktion'.format(antal, end - start))

# Sortera med Pythons inbyggda funktion
lista = [randint(0,4294967292) for i in range(antal)]
start = perf_counter()
lista.sort()
end = perf_counter()
print('Att sortera {:d} heltal tog {:f} sekunder med inbyggd sorteringsfunktion'.format(antal, end - start))