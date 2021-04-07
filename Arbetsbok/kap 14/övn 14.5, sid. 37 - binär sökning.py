#!/usr/local/bin/python3.9

# Filnamn: övn 14.2, sid. 36 - söka tal med funktion.py

# Sökning
# Programmeringsövningar till kapitel 14

# Programmet utgår från en befintlig och sorterad lista av tal och som också 
# skrivs ut på skärmen. Därefter frågar programmet användaren efter ett tal som 
# ska eftersökas. Slutligen undersöker programmet om talet finns i listan och 
# om det finns, skriver det ut vilket indexet det finns på. Om inte talet finns
# så ska användaren informeras om att det inte finns.
# 
# I exemplet använder jag sökmetoden Binär sökning

# Import av modul

# Funktionsdefinitioner
def binSok(listan, tal):
    # Utför en binär sökning genom listan
    # Utgå ifrån att talet inte finns
    mittenIdx = len(listan) // 2
    # Sätt undre index till början av listan 
    undreIdx = 0 
    # Sätt slutet av listan som övre index
    övreIdx = len(listan) - 1
    index = mittenIdx


    while index <= övreIdx:
        if tal > listan[index]:
            undreIdx = index + 1
            mittenIdx = (undreIdx + övreIdx) // 2
            index = mittenIdx
        if tal < listan[index]:
            övreIdx = index - 1
            mittenIdx = (undreIdx + övreIdx) // 2       
            index = mittenIdx
        if tal == listan[index]:
            # Om talet hittas sätt index till det och avbryt loopen
            return index
        index += 1
    # Returnera index för talet till anropande funktion
    return -1

# Huvudprogram
def main():
    # Initiera en lista med 14 sorterade tal
    lista = [3,7,14,19,21,40,47,47,69,72,83,87,94,101]

    # Skriv ut listan
    print(lista)

    # Fråga användaren efte tal som eftersöks
    tal = int(input('Anget tal som eftersöks: '))
    
    index = binSok(lista, tal)

    if index >= 0:
        print('Talet ' + str(tal) + ' finns på index ' + str(index) + ' i listan.')
    else:
        print('Talet ' + str(tal) + ' finns inte i listan.')

## Huvudprogram anropas 
main()