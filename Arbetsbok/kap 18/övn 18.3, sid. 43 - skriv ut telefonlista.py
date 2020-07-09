#!/usr/bin/python3.8

# Filnamn: övn 18.3, sid. 43 - skriv ut telefonlista.py

# Filhantering
# Programmeringsövningar till kapitel 18

# Programexempel som skriver ut telefonlista.txt i två kolumner
# <--------------- forts. här
def mataInLista(l):
    # För att spara antal kodrader använder jag den nya valross operatorn
    while rad := input('Ange namn och telefonnr separerat med mellanslag (tom rad avslutar): '):
        # Expandera listan genom att spara namn och telefonnr på varsit 
        # nytt index [0] = namn, [1] = telefonnr, [2] = namn ...
        l.extend(rad.split(' ', 1))
        # Returnera referens till den nya listan
    return l

# Skriv ut programrubrik
def skrivutRubrik():
    print('TELEFONLISTA')
    print('============')
    print()

# Öppna och läs in hela filen till minnet med felhantering
def oppnaLasFil(fn):
    global rad
    global filinnehall
    fn = './' + fn # För att hitta filen i linux, måste ev. ändras på windows till ''
    try: 
        # Öppna och läs in hela filen    
        with open(fn, 'r', encoding = 'utf-8') as f: 
            filinnehall = f.read()
    except FileNotFoundError:
        print('Fel - hittar inte filen', fn, 'som ska öppnas.')
        rad += 1
        return -1 # Tala om för anropande rutin att det inte gick att öppna filen
    else:
        # Stäng filen och returnera hela filinnehållet
        f.close() 
        return filinnehall

# öppnar filen med en säkrare sk kontex öppning, om inte filen 
# finns skapas den, w = skriver och ersätter tidigare innehåll
def oppnaSkrivFil(fn,l):
    fn = './' + fn # För att hitta filen i linux, måste ev. ändras på windows till ''
    try:
        with open(fn, 'w', encoding = 'utf-8') as f:
            # Loopa igenom listan för varje angivet namn, sista namnet står i listan - 1 i listans index, inkrmetering med 2 för att fånga varje namn
            for n in range(0, len(l)-1,2):
                f.write(l[n] + '\n')        # Skriv namnet + nyradstecken
                f.write(l[n + 1] + '\n')    # Därefter skrivs telefonnr + nyradstecken
            # Stäng filen efter all skrivning
            f.close()
    # Filen är antingen skrivskyddad eller öppen i ett annat program och systemet kan ej hantera detta utan exklusiv åtkomst
    except PermissionError:
        print('Fel - Kunde inte öppna fil. Antingen är den skrivskyddad eller öppnad med ett annat program.')

# Programmets huvudloop
def main():
    # Variabeldeklarationer
    helaListan = []  
    
    # Skrivut programrubrik
    skrivutRubrik()

    # Läs in filens innehåll och lagra det i listan  
    helaListan = oppnaLasFil('telefonlista.txt')

# Programmet startar här
main()