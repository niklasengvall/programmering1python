#!/usr/bin/python3.8

# Filnamn: övn 9.8 - fibonaccis talföljd - kap. 9, sid. 23.py

# Funktioner
# Programmeringsövningar till kapitel 9

# Programmet beräknar fibonaccis talföljd och lita annat runt detta, se 
# funktionsbeskrivingar nedan

# Importera nödvändiga funktioner och konstanter
from math import sqrt

# Funktionsdefinitioner
def fibLista(antal):        
    """ Räknar ut fibonaccital och placerar dem i en lista.

        antal : integer
            Hur många fibonaccital som ska lagras i listan

        returvärde : integer
            Returnerar referens till anropande argument med listan.
    """
    lista = [1, 1]
    for i in range(2,40):
        lista.append(lista[i-2]+lista[i-1])

    
    return lista

def fibTal(index):        
    """ Räknar ut fibonaccital med index nr 0 är första numret.

        index : integer
            Vilket fibonacci tal i ordningen ska vi räkna ut
            0 är första talet

        returvärde : integer
            Returnerar fibbonaccitalet på indexnr.
    """

    tal1 = 1
    tal2 = 1
    
    for i in range(index):
        if index == 0:
            tal3 = 1
            break
        elif index == 1:
            tal3 = 1
            break
        tal3 = tal2 + tal1 # Ok
              
        tmp = tal2
        tal2 = tal3
        tal1 = tmp

    return tal3

# Huvudprogram
def main():
    
    # övn 9.8 a) Beräkna och lagra de 40 första talen i fibonaccis talföljd 
    # i en lista
    lista40 = fibLista(40)          
    # Skriv ut listan
    print(lista40)

    # övn 9.8 b) Skriv ut kvoten mellan talet och föregående tal för fibonaccis listans tal 2 till listans sista tal 
    for i in range(1, len(lista40)):
        kvot = lista40[i] / lista40[i-1]
        print(i,':',kvot)
    print()
    
    # övn 9.8 c) Beräkning av talet fi - Det gyllene snittet
    fi = (1 + sqrt(5)) / 2
    print('Talet fi =',fi)

    # övn 9.8 d) Beräkna fibbonacci talet med index nr, där 0 är första talet 
    print('Fibonaccital nr', 7, 'är',fibTal(6))

## Huvudprogram anropas
main() 