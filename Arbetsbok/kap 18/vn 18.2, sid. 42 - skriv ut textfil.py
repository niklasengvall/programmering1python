#!/usr/bin/python3.7

# Filnamn: övn 18.2, sid. 42 - skriv ut textfil.py

# Filhantering
# Programmeringsövningar till kapitel 18

# Programmet frågar användaren efter en sökväg samt filnamn till en textfil. 
# Går ej filen att öppna ska ett felmeddelande skrivas och användaren ska få 
# möjlighet att antingen avbryta eller ange en ny sökväg med filnamn.


# Import av modul

# Funktionsdefinitioner
def meny():
    print('Vad vill du göra?')
    print('===================================')
    print('1. lägga till eller ändra en adress')
    print('2. söka en adress')
    print('3. ta bort en adress ur listan')
    print('4. visa hela registret')
    print('0. avsluta\n')
  
def avsluta():
    exit()

def laggTill():
    print()
    nyckel = input('Ange namn: ')
    värde = input('Ange e-postadress: ')
    nyckel = nyckel.capitalize()
    värde = värde.lower()
    adresser[nyckel] = värde
    print()

def sok():
    print()
    nyckel = input('Ange namn på den adress du vill söka efter: ')
    nyckel = nyckel.capitalize()
    if nyckel in adresser:
        print('Namnet', nyckel, 'finns.')
    else:
        print('Ingen med namn', nyckel,'finns.')
    print()

def tabort():
    print()
    nyckel = input('Ange namn på den adress du vill ta bort: ')
    nyckel = nyckel.capitalize()
    print('Tar bort addressen', adresser[nyckel])
    del(adresser[nyckel])
    print()

def visa():
    print()
    for nyckel, värde in adresser.items():
        print('Namn:', nyckel,'e-post:', värde)
    print()

    # Huvudprogram
def main():
    # Skriv ut meny
    meny()
    # Fråga vad användaren vill
    while True:
        val = input('Välj 1 - 4 eller 0: ')
        if val == '0':
            avsluta()
        elif val == '1':
            laggTill()
            meny()
        elif val == '2':
            sok()
            meny()
        elif val == '3':
            tabort()
            meny()
        elif val == '4':
            visa()
            meny()
        
# Huvudprogram anropas 
adresser = {}
main()