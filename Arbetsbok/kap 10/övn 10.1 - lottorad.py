#!/usr/bin/python3.8

# Filnamn: övn 10.1 - lottorad.py

# Slumptal i programmering
# Programmeringsövningar till kapitel 10

# Programmet slumpar fram en lottorad, 7 tal i intervallet 1 - 35 där samma 
# nummer inte får uppkomma 2 gånger

from random import randrange
# Funktionsdefinitioner
def lottorad():        # Funktionshuvud
    
    # Variabeldeklarationer
    tal = 0 # Lagrar ett slumptal temporärt
    lottorad = [0, 0, 0, 0, 0, 0, 0] # Lottorad som ska returneras senare
    i = 0
    
    # Slumpa fram 7 tal mellan 1-35 och lagra i listan lottorad
    # talen som lagras måste vara olika
    while i < 7: 
        tal = randrange(1,36)      
        lottorad[i] = tal
        i += 1
        # Kontroll om tal finns som dublett
        for c in range(i):
            # om tal och listans tal c är lika och c samt i-1 är skilda från
            # varandra då är det en dublett 
            if tal == lottorad[c] and c != (i-1):
                # Vi ska fixa ett nytt slumptal på samma index
                # då det gamla var en dublett därav i -1 och break
                i -= 1
                break
    # Återgå till anropande program med en sorterad lista
    return sorted(lottorad)

# Huvudprogram
def main():
    print(lottorad())
## Huvudprogram anropas 
main()