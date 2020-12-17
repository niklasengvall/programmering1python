#!/usr/local/bin/python3.9

# Filnamn: övn 18.6, sid. 43 - epostlista med sparfunktion.py

# Filhantering
# Programmeringsövningar till kapitel 18

# Programmet låter användaren mata in uppgifer till register över e-postadresser, vilka lagras i et dictionary. 
# Nycklarna ska vara namn och e-postadresserna värden. Vi låter användaren välja vad som ska göras genom ett menyval
# I denna övning så lägger jag till en funktion för att kontrollera så att e-postadressen innehåller minst 
# ett @ och en .
# När programmet startar så kontrollerar det om det sedan tidigare finns en sparad epostadresser2 och om så så läses den in.
# När användaren avslutar programmet så kontrolleras det om uppdateringar skett och frågar användaren om hen vill spara dessa.

# Import av moduler
import os, inspect # vi ska kunna få fram var denna skriptfil finns 

# Funktionsdefinitioner
def meny():
    print('Vad vill du göra?')
    print('===================================')
    print('1. lägga till eller ändra en adress')
    print('2. söka en adress')
    print('3. ta bort en adress ur listan')
    print('4. visa hela registret')
    print('0. avsluta\n')
  
def avsluta(fn, dic):
    skrivTillFil(fn,dic)
    exit()

def laggTill(adr):
    print()
    nyckel = input('Ange namn: ')
    värde = input('Ange e-postadress: ')
    while True:
        if check(värde):
            break
        else:
            värde = input('Du angav en ogiltig e-postadress, försök igen: ')          

    nyckel = nyckel.capitalize() # Gör 1:a bokstav stor
    värde = värde.lower() # Gör om hela e-postadressen till små bostäver
    adr[nyckel] = värde     
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

def sok(adr):
    print()
    nyckel = input('Ange namn på den adress du vill söka efter: ')
    nyckel = nyckel.capitalize()
    if nyckel in adr:
        print('Namnet', nyckel, 'finns.')
    else:
        print('Ingen med namn', nyckel,'finns.')
    print()

def tabort(adr):
    print()
    nyckel = input('Ange namn på den adress du vill ta bort: ')
    nyckel = nyckel.capitalize()
    if nyckel in adr:
        print('Tar bort addressen', adr[nyckel])
        del(adr[nyckel])
    else:
        print('Ingen med namn', nyckel,'finns.')
    print()

def visa(adr):
    print()
    print("Namn                 E-post")
    for nyckel, värde in adr.items():
        attSkrivaUt = "%-20s %s" %(nyckel, värde) # Skriv ut namn vänsterjusterat och reservera 20 tecken för att få raka kolumner
        print(attSkrivaUt)     
    print()

# Checka om fil finns, om så returnera sant
def finnsFil(fn):
    # Ta fram fullständig sökväg till filen som ska öppnas
    fn = hamtaSokvag() + '/' + fn
    if os.path.isfile(fn):
        return True
    else:
        return False 

# Skriv filen med en säkrare sk kontex öppning, om inte filen 
# finns skapas den, w = skriver och ersätter tidigare innehåll
def skrivTillFil(fn,l):
    # Ta fram fullständig sökväg till filen som ska skrivas
    fn = hamtaSokvag() + '/' + fn
    try:
        with open(fn, 'w', encoding = 'utf-8') as f:
            # Loopa igenom dictinary för varje angiven e-postadress
            for n,a in l.items():
                f.write(n + '\n') # Skriv namnet + nyradstecken
                f.write(a + '\n') # Skriv e-postadressen + nyradstecken

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
    fil = inspect.getframeinfo(inspect.currentframe()).filename
    return os.path.dirname(os.path.abspath(fil))


# Huvudprogram
def main():
    # Variabeldeklarationer
    filnamn = "epostadresser2.txt" # i denna fil ska vi spara adresserna
    adresser = {} # Initiera en dictionary adresser
    filinnehåll = []
    
    # Om fil sparad telefonlista finns läs in filens innehåll till dictinary annars lämnas den tom
    if finnsFil(filnamn):
        print("Fil finns!")
    else:
        print("Fil finns inte!")
    # Läs in 
    #filinnehåll = oppnaLasFil(filnamn)
    
    # Dela upp listan så att vi får ett nytt element efter varje nyradstecken
    #inlasta_slumptal = inlasta_slumptal.splitlines()
    
    # Skriv ut meny
    meny()
    # Fråga vad användaren vill
    while True:
        val = input('Välj 1 - 4 eller 0: ')
        if val == '0':
            avsluta(filnamn, adresser)
        elif val == '1':
            laggTill(adresser)
        elif val == '2':
            sok(adresser)
        elif val == '3':
            tabort(adresser)
        elif val == '4':
            visa(adresser)
        meny()
        
# Huvudprogram anropas 
main()