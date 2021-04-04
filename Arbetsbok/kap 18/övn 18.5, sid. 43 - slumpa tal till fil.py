#!/usr/local/bin/python3.9

# Filnamn: övn 18.5, sid. 43 - slumpa tal till fil.py

# Filhantering
# Programmeringsövningar till kapitel 18

# Programexempel som slumpar 20 heltal mellan 1 - 100 och skriver dessa till en
# textfil. Därefter läses desssa tal in till en lista och till sist skrivs listan ut


import random, os, inspect # Vi ska hantera slumptal och kunna få fram var denna skriptfil finns

# Funktionsdefinitioner
 
# Funktion för att skapa 20 st slumptal och spara dem strängformaterade i en lista
def skapaSlumptal(a, ns):
    random.seed()
    for antal in range(a):
        ns.append(random.randint(1,100))
    # Sortera listan, obs. ingick ej i uppgiften, men det blir snyggare så
    ns.sort()
    # Gör om listans numeriska element till strängelement
    for antal in range(a):
        ns[antal] = str(ns[antal])
    return ns

# öppnar filen med en säkrare sk kontex öppning, om inte filen 
# finns skapas den, w = skriver och ersätter tidigare innehåll
def skrivTillFil(fn,l):
    # Ta fram fullständig sökväg till filen som ska skrivas
    fn = hamtaSokvag() + '/' + fn
    try:
        with open(fn, 'w', encoding = 'utf-8') as f:
            # Loopa igenom listan för varje slumptal
            for n in range(0, len(l)):
                f.write(l[n] + '\n') # Skriv slumptalet + nyradstecken
            # Stäng filen efter all skrivning
            f.close()
    # Filen är antingen skrivskyddad eller öppen i ett annat program och systemet kan ej hantera detta utan exklusiv åtkomst
    except PermissionError:
        print('Fel - Kunde inte öppna fil. Antingen är den skrivskyddad eller öppnad med ett annat program.')

# Öppna och läs in hela filen till minnet med felhantering
def oppnaLasFil(fn):
   
    # Ta fram fullständig sökväg till filen som ska öppnas
    fn = hamtaSokvag() + '/' + fn
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

# Ta fram sökvägen till denna skriptfil och lägg det till filnamnet som ska öppnas
# Förutsätter att den sparade filen finns i samma mapp som denna skriptfil
# Möjliggör att vi kan köra skriptet från annan aktiv arbetsmapp
def hamtaSokvag():
    filename = inspect.getframeinfo(inspect.currentframe()).filename
    return os.path.dirname(os.path.abspath(filename))

# Programmets huvudloop
def main():
    # Variabeldeklarationer
    nya_slumptal = []
    inlasta_slumptal = []
    filnamn = "20 slumptal.txt"

    # Skapa 20 st slumptal och lagra dem i en lista
    nya_slumptal = skapaSlumptal(20, nya_slumptal)
    
    # Skriv slumptalen till en fil
    skrivTillFil(filnamn, nya_slumptal)
    
    # Meddela vilka tal som skrevs till filen
    print(f'Följande slumptal skrevs till filen: {filnamn}')
    print(nya_slumptal)

    # Läs in filens innehåll till en lista
    inlasta_slumptal = oppnaLasFil(filnamn)
    
    # Dela upp listan så att vi får ett nytt element efter varje nyradstecken
    inlasta_slumptal = inlasta_slumptal.splitlines()
    
    # Skriv ut listan med slumptal
    print()
    print(f'Följande slumptal lästes från filen: {filnamn}')
    print(inlasta_slumptal)

# Programmet startar här
main()