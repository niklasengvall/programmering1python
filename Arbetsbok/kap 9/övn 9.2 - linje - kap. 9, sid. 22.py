#!/usr/local/bin/python3.9

# Filnamn: övn 9.2 - linje - kap. 9, sid. 22.py

# Funktioner
# Programmeringsövningar till kapitel 9

# Programmet innehåller en funktion linje(antal) som skriver ut antal understrykningsstreck i terminalfönstret

# Funktionsdefinitioner
def linje(antal):        
    """ Ritar ut en linje med hjälp av understreck i konsolfönstret

    antal : integer
        Antalet understreck som linjen ska bestå av
    """

    print(antal * '_')

# Huvudprogram
def main():
    # Skriv ut en linje med 30 st understreck
    linje(30)

## Huvudprogram anropas
main()