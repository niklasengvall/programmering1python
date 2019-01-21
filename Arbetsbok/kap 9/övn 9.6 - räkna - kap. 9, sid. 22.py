#!/usr/bin/python3.7

# Filnamn: övn 9. 6 - räkna - kap. 9, sid. 22.py

# Funktioner
# Programmeringsövningar till kapitel 9

# Programmet frågar efter två operander och operator, därefter beräknar 
# programmet resultatet 

# Funktionsdefinitioner
def calc(tal1, tal2, operator):        
    """ Beräknar tal1 och tal2 med önskad operator

        Du kan använda operatorerna +, -, * och / 
        
        tal1: float
            Operand 1

        tal2: float
            Operand 2

        returvärde : float
            Returnerar resultatet av beräkningen.
    """
    
    # Undersök vilken form av beräkning och utför den
    if operator == '+':
        beräkning = tal1 + tal2
    elif operator == '-':
        beräkning = tal1 - tal2
    elif operator == '*':
        beräkning = tal1 * tal2
    elif operator == '/':
        beräkning = tal1 / tal2
    else:
        beräkning = None
    return beräkning

# Huvudprogram
def main():
    # Variableinitieringar där priser tilldelas värden av typen float
    tal1 = float(input('Ange tal1: '))
    tal2 = float(input('Ange tal2: '))
    operator = input('Ange operator (+, -, *, /): ')

    resultat = calc(tal1, tal2, operator)

    # Formaterad utskrift med två decimaler, kronor och ören.
    print('Resultatet av beräkningen blev:', resultat)
    
## Huvudprogram anropas
main() 