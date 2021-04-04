#!/usr/local/bin/python3.9

# Filnamn: övn 10.2 - stryktipsrad.py

# Slumptal i programmering
# Programmeringsövningar till kapitel 10

# Programmet slumpar fram en stryktipsrad, 13 tal i intervallet 1-3 där 1 är 1 
# och 2 är X och 3 är 2 vid utskrift på skärmen 

from random import randrange
# Funktionsdefinitioner
def stryktipsrad(a, b, c):  # Funktionshuvud
    
    # Variabeldeklarationer
    tal = 0 # Lagrar ett slumptal temporärt
    chans = 0 # Sannolikhet
    stryktipsrad = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
    översätt = {1: '1', 2: 'X', 3: '2'}
    
    i = 0
    
    # Slumpa fram 13 tal mellan 1-3 och lagra i listan stryktipsrad
    while i < 13: 
        chans = randrange(1,101)
        if chans <= a:
            tal = 1
        elif chans > a and chans <= ( a + b):
            tal = 2 
        elif chans > (a + b) and chans <= (a + b + c):
            tal = 3 
        
        stryktipsrad[i] = översätt[tal]
        i += 1

    # Återgå till anropande program 
    return stryktipsrad

def skrivutRad(lista):
    for i in range(len(lista)):
        if lista[i] == '1':
            print(str(lista[i]) + '    ')
        elif lista[i] == 'X':
            print('  ' + str(lista[i]) + '  ')
        elif lista[i] == '2':
            print('    ' + str(lista[i]))

# Huvudprogram
def main():
    # a) 33 % chans till 1, 33 % till x och 33 % till 2 
    print('a)')
    skrivutRad(stryktipsrad(33,33,33))

    print()
    print('b)')
    # b) 50 % chans till 1, 25 % till x och 25 % till 2 
    skrivutRad(stryktipsrad(50,25,25))

## Huvudprogram anropas 
main()
