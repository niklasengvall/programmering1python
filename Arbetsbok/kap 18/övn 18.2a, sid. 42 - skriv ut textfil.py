#!/usr/bin/python3.8

# Filnamn: övn 18.2a, sid. 42 - skriv ut textfil.py

# Filhantering
# Programmeringsövningar till kapitel 18

# Programmet frågar användaren efter en sökväg samt filnamn till en textfil. 
# Går ej filen att öppna ska ett felmeddelande skrivas och användaren ska få 
# möjlighet att antingen avbryta eller ange en ny sökväg med filnamn.


# Import av modul

# Funktionsdefinitioner
def rubrik():
    print('Program som skriver ut en textfil till skärmen')
    print('==============================================')
    print()
  
def fragaFilnamn():
    # Testa om användaren anger mint ett tecken
    filnamn = input('Ange filnamn: ')
    while len(filnamn) == 0:
        print('FEL: Ett filnamn består av minst ett tecken.')      
        filnamn = input('Ange filnamn: ')
    return filnamn

def oppnaFil(fn):
    fn = './' + fn # För att hitta filen i linux 
    try: 
        # Öppna och läs in hela filen    
        with open(fn, 'r', encoding = 'utf-8') as f:
            filinnehåll = f.read()
    except FileNotFoundError:
        print('Fel - hittar inte filen', fn, 'som ska öppnas.')
        return -1 # Tala om för anropande rutin att det inte gick att öppna filen
    else:
        print(filinnehåll)
        f.close()

    # Huvudprogram
def main():
    # Skriv ut rubrik
    rubrik()

    # Fråga efter filnamn   
    filnamn = fragaFilnamn()
    
    # Öppna filen
    while resultat := oppnaFil(filnamn) == -1: # Kör loop så länge det inte går att öppna fil 
        while True: # Fråga om och om igen, tills användaren anger J eller N
            print('Vill du försöka igen (J) eller avbryta programmet (N)?')
            svar = input('Svara (J/N)? ')
            if svar == 'N' or svar == 'n':
            # Avbryt while-loopen och hoppa ur programmet
                exit() 
            elif svar == 'J' or svar == 'j':
                filnamn = fragaFilnamn()
                break # För att lämna evighetsloopen och gå tillbaka till loopen ovan
            
# Huvudprogram anropas 
main()