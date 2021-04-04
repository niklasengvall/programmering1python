#!/usr/local/bin/python3.9

# Filnamn: övn 14.1, sid. 36 - söka tal.py

# Sökning
# Programmeringsövningar till kapitel 14

# Programmet slumpar först fram 20 tal mellan 1 och 100 och lagrar alla talen i 
# en lista och sedan skrivs listan ut på skärmen. Därefter frågar programmet 
# användaren efter ett tal som ska eftersökas. Slutligen undersöker programmet 
# om talet finns i listan och om det finns, skriva ut på indexet det finns på.
# Om inte talet finns så ska användaren informeras om att det inte finns.

# Sökmetod: Linjär sökning

# Import av modul
from random import randint

# Funktionsdefinitioner

# Huvudprogram
def main():
    lista = []

    # Slumpa 20 st heltal mellan 1 och 100 och lägg dem eftervarandra i listan
    for c in range(20):
        lista.append(randint(1,100))
    # Skriv ut listan
    print(lista)

    # Fråga användaren efte tal som eftersöks
    tal = int(input('Anget tal som eftersöks: '))
    
    # Utför en linjär sökning i hela listan
    # Utgå ifrån att talet inte finns
    index = -1
    for i in range(len(lista)):
        if tal == lista[i]:
            # Om talet hittas sätt index till det och avbryt loopen
            index = i
            break

    if index >= 0:
        print('Talet ' + str(tal) + ' finns på index ' + str(index) + ' i listan.')
    else:
        print('Talet ' + str(tal) + ' finns inte i listan.')

## Huvudprogram anropas 
main()