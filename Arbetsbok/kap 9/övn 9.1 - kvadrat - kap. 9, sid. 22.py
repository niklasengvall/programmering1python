#!/usr/local/bin/python3.9

# Filnamn: övn 9.1 - kvadrat - kap. 9, sid. 22.py

# Funktioner
# Programmeringsövningar till kapitel 9

# Programmet innehåller en funktion kvadrat(tal) som beräknar och returnerar 
# argumentet tals kvadrat

# Funktionsdefinitioner
def kvadrat(tal):        # Funktionshuvud
    return tal * tal

# Huvudprogram
def main():
    tal = float(input('Ange ett tal du vill kvadrera: '))
    print('Talet', tal, 'blir i kvadrat:', kvadrat(tal))

## Huvudprogram anropas
main()