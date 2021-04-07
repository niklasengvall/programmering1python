#!/usr/local/bin/python3.9

# Filnamn: övn 15.3, sid. 39 - sortera svenska namn.py

# Sortering
# Programmeringsövningar till kapitel 15

# Programmet utför bubbelsortering och avbryter om inga efternamn bytt plats under 
# ett pass, varje pass blir också kortare 

# Import av modul
from time import perf_counter # Används för att mäta tid

# Funktionsdefinitioner
def bubbelsortering(lista):
    index = 0
    byttPlats = False
    maxPass = len(lista) - 1
    antalPass = 0
    while antalPass <= maxPass:
        if lista[index].translate(svTabell) > lista[index + 1].translate(svTabell):
            lista[index], lista[index + 1] = lista[index + 1], lista[index]
            byttPlats = True  
        index += 1
        # Hoppas över de redan sorterade talen i slutet av vektorn
        if index >= maxPass - antalPass:
            if byttPlats == False:
                break
            else:
                index = 0
                byttPlats = False
                antalPass += 1

# Huvudprogram
def main():

    # Lista att sortera
    efternamn = ['Åberg', 'Öberg', 'Viklund', 'andersson', 'Anderberg', 'Ärleskog', 'Sträng', 'Stråby', 'viklander', 'Engvall']
    listLängd = len(efternamn)
    start = perf_counter() # Start för tidsmätning
    bubbelsortering(efternamn)
    end = perf_counter()   # Slut för tidsmätning
    print(efternamn)
    print(f'Att sortera {listLängd:d} efternamn tog {(end-start):f} sekunder med inbyggd sorteringsfunktion')

# Huvudprogram anropas 
# Översättningstabell för att jämföra svenska strängar
svTabell = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖåäöéÉàÀüÜ', 
                         'abcdefghijklmnopqrstuvwxyz{|}{|}eeaayy')
main()
