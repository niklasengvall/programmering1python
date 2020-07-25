#!/usr/local/bin/python3.8

# Filnamn: övn 16.2, sid. 40 - register.py

# Mer om listor samt dictionarier
# Programmeringsövningar till kapitel 16

# Programmet låter användaren mata in uppgifer till register över e-postadresser, vilka lagras i et dictionary. 
# Nycklarna ska vara namn och e-postadresserna värden. Vi låter användaren välja vad som ska göras genom ett menyval
# I denna övning så lägger jag till en funktion för att kontrollera så att e-postadressen innehåller minst 
# ett @ och en .

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
    while True:
        if check(värde):
            break
        else:
            värde = input('Du angav en ogiltig e-postadress, försök igen: ')          

    nyckel = nyckel.capitalize()
    värde = värde.lower()
    adresser[nyckel] = värde
        
    print()

def check(epost):
    value = 0
    var = epost.find('@') # returnera indexpos där @ finns
    if var > 0: # om man skrivit @ som tecken nr 2 så är det ok
        value += 1
    if epost.find('.') > (var + 1): # punkten måste ligga bakom @ + ett tecken till
        value += 1
    
    if value == 2: # finns både @ och . då ska vi returnera att e-postadresen är korrekt skriven
        return True
    else:
        return False

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