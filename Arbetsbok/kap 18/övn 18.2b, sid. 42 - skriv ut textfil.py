#!/usr/local/bin/python3.9

# Filnamn: övn 18.2b, sid. 42 - skriv ut textfil.py

# Filhantering
# Programmeringsövningar till kapitel 18

# Programmet frågar användaren efter en sökväg samt filnamn till en textfil. 
# Går ej filen att öppna ska ett felmeddelande skrivas och användaren ska få 
# möjlighet att antingen avbryta eller ange en ny sökväg med filnamn.
# Raderna numreras i vänsterkant och skrivs ut på skärmen, när man når sista raden 
# i terminalen pausas utskriften och man får trycka ENTER för att se nästa rad

# Import av modul - för att ta reda på antal rader som min terminal använder samt skicka rensa konsol kommando
# system - för att köra operativsystemsspecifika kommandon
# name - innehåller operativsystemets namn
# get_terminal_size - funktion som returnerar en tuppel med terminalens kolumn och rad storlek
from os import system, name, get_terminal_size
# Funktionsdefinitioner

# Rensar terminalfönstret på windows, linux och mac 
def rensaSkarm(): 
    global rad # Hänvisa till global modulvariabel
    # Windows - Om operativsystemets namn är nt, kör kommandot cls
    if name == 'nt': 
        system('cls') 
    # Mac och Linux - Om operativsystemets namn är posix, kör kommandot clear
    else: 
        system('clear')
    rad = 0  

# Skriv ut programrubrik
def rubrik():
    global rad 
    print('Program som skriver ut en textfil till skärmen')
    print('==============================================')
    print()
    rad += 3 # ökar radpositionen för var vi är i terminalen
  
# Fråga användaren efter ett filnamn som de får mata in och returnera till anropande rutin
def fragaFilnamn():
    global rad
    global rader
    # Testa om användaren anger mint ett tecken, annars fråga igen
    filnamn = input('Ange filnamn: ')
    rad += 1
    while len(filnamn) == 0:
        print('FEL: Ett filnamn består av minst ett tecken.')
        filnamn = input('Ange filnamn: ')
        rad += 2
    return filnamn

# Öppna och läs in hela filen till minnet med felhantering
def oppnaFil(fn):
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


    # Huvudprogram
def main():
    global rad
    global rader
    global filinnehall
    # Rensa terminalfönstret
    rensaSkarm()

    # Skriv ut rubrik
    rubrik()
    
    # Spara terminalens storlek
    (kolumner, rader) = get_terminal_size() 

    # Fråga efter filnamn   
    filnamn = fragaFilnamn()
    
    # Öppna filen
    while resultat := oppnaFil(filnamn) == -1: # Kör loop så länge det inte går att öppna fil 
        while True: # Fråga om och om igen, tills användaren svarar J eller N
            print('Vill du försöka igen (J) eller avbryta programmet (N)?')
            svar = input('Svara (J/N)? ')
            rad += 2
            if svar == 'N' or svar == 'n':
                # Avbryt while-loopen och hoppa ur programmet
                exit() 
            elif svar == 'J' or svar == 'j':
                filnamn = fragaFilnamn() 
                break # För att lämna inre evighetsloop och gå tillbaka till loopen ovan
    
    # Skriv ut filens innehåll
    line = "" # Används för att lagra en rad text
    n = 1     # Radnrräknare för textfilens rader  
    for r in filinnehall:       # Gå igenom filinnehållet tecken för tecken
        if r != '\n':           # Så länge tecknet inte är et nyrads-tecken
            line += r           # Skapa en sammanhängande rad med text
        else:
            print(n, line)      # När ny radstecken kommer, skriv ut radnr framför textraden
            line = ""           # Återställ och gör radsträngen tom
            rad += 1            # Öka radnr
            if rad >= rader-1:  # Om rad räknare är lika med terminalhöjd i rader - 1 
                input('')       # Vänta på att användare trycker ENTER, detta tar en rad i anspråk
                rad += 2        # Därför ökar vi radräknaren med 2
            n += 1              # Öka nr som ska skriva ut framför textraden med 1

# Huvudprogram anropas 
rad = 0             # Global variabel som används för att räkna antal rader så paus sker när terminalens sista rad nås
rader = 0           # Global variabel för att hålla koll på din terminals antal rader
filinnehall = ""    # Global variabel som innehåller filens text

main()