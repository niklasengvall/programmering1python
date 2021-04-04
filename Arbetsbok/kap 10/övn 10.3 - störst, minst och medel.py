#!/usr/local/bin/python3.9

# Filnamn: övn 10.3 - störst, minst och medel.py

# Slumptal i programmering
# Programmeringsövningar till kapitel 10

# Programmet slumpar fram 100 tal mellan 1 och 1000. Därefter skrivs största, 
# minsta och medelvärdet ut gällande dessa tal.

from random import randrange
# Funktionsdefinitioner
def slumpatal(antal, start, slut):  # Funktionshuvud
    
    # Variabeldeklarationer
    lista = []
    
    # Skapa en lista innehållandes  antal slumpade tal mellan start och slut
    for i in range(antal):
        lista.append(randrange(start,slut))

    # Återgå till anropande program med en lista
    return lista

def medelvärde(lista):
    summa = 0
    antal = len(lista) 

    # Beräkna listans totalsumama
    for i in range(antal):
        summa += lista[i]

    return summa / antal

# Huvudprogram
def main():
    minsta = 0
    största = 0
    medel = 0

    lista = slumpatal(101,1,1001)
    minsta = min(lista)
    största = max(lista)
    medel = medelvärde(lista)
    
    print(lista)
    print('Minsta värde:', minsta)
    print('Största värde:', största)
    print('Medelvärde:', medel)

## Huvudprogram anropas 
main()
