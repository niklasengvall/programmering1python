#!/usr/bin/python3.8

# Filnamn: övn 18.3, sid. 42 - namn och telnr.py

# Filhantering
# Programmeringsövningar till kapitel 18

# Programexempel som frågar efter namn och telefonnr upprepat tills raden lämnas tom.
# Därefter lagras namn och telefonnr på varannan rad i en textfil telefonlista.txt

def mataInLista(l):
    # För att spara antal kodrader använder jag den nya valross operatorn
    while rad := input('Ange namn och telefonnr separerat med mellanslag (tom rad avslutar): '):
        # Expandera listan genom att spara namn och telefonnr på varsit 
        # nytt index [0] = namn, [1] = telefonnr, [2] = namn ...
        l.extend(rad.split(' ', 1))
        # Returnera referens till den nya listan
    return l

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
    lista = []  
    helaListan = mataInLista(lista)   
    oppnaSkrivFil('telefonlista.txt', helaListan)

# Programmet startar här
main()