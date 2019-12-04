#!/usr/local/bin/python3.7

# Filnamn: övn 16.1, sid. 40 - register.py

# Mer om listor samt dictionarier
# Programmeringsövningar till kapitel 16

# Programmet låter användaren mata in uppgifer till register över e-postadresser, vilka lagras i et dictionary. 
# Nycklarna ska vara namn oc e-postadresserna värden. Vi låter användaren välja vad som ska göras genom ett menyval


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