#!/usr/local/bin/python3.9

# Filnamn: övn 9.7 - cirkelns radie - kap. 9, sid. 22.py

# Funktioner
# Programmeringsövningar till kapitel 9

# Programmet frågar efter cirkelns area och räknar ut med hjälp av en funktion 
# cirkelns radiet

# Importera nödvändiga funktioner och konstanter
from math import pi, sqrt

# Funktionsdefinitioner
def cirkelradie(cirkelarea):        
    """ Räknar ut cirkelns radie utifrån dess area.

        Formeln för cirkelarea = pi*radie**2 => 
                    radie = sqrt(cirkelarea / pi)
      
        cirkelarea: float
            Cirkelns area i enheten ae (areaenheter)

        returvärde : float
            Returnerar cirkelns radie.
    """
    return sqrt(cirkelarea / pi)

# Huvudprogram
def main():
    # Fråga användaren hur stor area cirkeln har
    area = float(input('Ange cirkelns area (ae): '))
    
    # Beräkna radien
    radie = cirkelradie(area)
        
    # Formaterad utskrift med två decimaler, kronor och ören.
    print('En cirkel med arean ' + str(area) + ' ae, har radien ' + str(radie) + ' le.')

## Huvudprogram anropas
main() 