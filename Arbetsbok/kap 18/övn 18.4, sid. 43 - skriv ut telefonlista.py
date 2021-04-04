#!/usr/local/bin/python3.9

# Filnamn: övn 18.4, sid. 43 - skriv ut telefonlista.py

# Filhantering
# Programmeringsövningar till kapitel 18

# Programexempel som skriver ut telefonlista.txt i två kolumner

import os, inspect # För att få fram var denna skriptfil finns

# Skriv ut programrubrik
def skrivutRubrik():
    print('TELEFONLISTA')
    print('============')
    print()

# Öppna och läs in hela filen till minnet med felhantering
def oppnaLasFil(fn):
    # Ta fram sökvägen till denna skriptfil och lägg det till filnamnet som ska öppnas
    # Förutsätter att den sparade telefonlistan finns i samma mapp som denna skriptfil
    # Möjliggör att vi kan köra skriptet från annan aktiv arbetsmapp

    filename = inspect.getframeinfo(inspect.currentframe()).filename
    path = os.path.dirname(os.path.abspath(filename))

    fn = path + '/' + fn # För att hitta filen i linux, måste ev. ändras på windows till ''
    try: 
        # Öppna och läs in hela filen    
        with open(fn, 'r', encoding = 'utf-8') as f: 
            filinnehall = f.read()
    except FileNotFoundError:
        print('Fel - hittar inte filen', fn, 'som ska öppnas.')
        return -1 # Tala om för anropande rutin att det inte gick att öppna filen
    else:
        # Stäng filen och returnera hela filinnehållet
        f.close() 
        return filinnehall

def skrivTvaKolumner(fi):
    # Dela upp listan så att vi får ett nytt element efter varje nyradstecken
    fi = fi.splitlines()

    #Skriv ut Listan i 2 kolumner som är 15 tecken breda
    for n in range(0, len(fi)-1,2):
        print(f'{fi[n]:{15}}{fi[n + 1]:{15}}') # n = namnet, n + 1 = telefonnr

# Programmets huvudloop
def main():
    # Variabeldeklarationer
    filinnehall = []  
    
    # Skriv ut programrubrik
    skrivutRubrik()

    # Läs in filens innehåll
    filinnehall = oppnaLasFil("telefonlista.txt")
    
    #Skriv ut Listan i 2 kolumner
    skrivTvaKolumner(filinnehall)

# Programmet startar här
main()