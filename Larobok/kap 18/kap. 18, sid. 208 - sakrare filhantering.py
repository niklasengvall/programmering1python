#!/usr/bin/python3.8

# Filnamn: kap. 18, sid. 208 - säkrare filhantering.py

# Kapitel 19 - Filhantering
# Programmering 1 med Python - Lärobok

# Kodexempel från boken med förklaringar

# Enkelt programexempel som visar skrivning och läsning av
# en textfil. Först öppnar vi filen för skrivning och
# skriver dit något

# öppnar filen med en säkrare sk kontex öppning, om inte filen 
# finns skapar den, w = skriver och ersätter tidigare innehåll
try:
    with open('./test.txt', 'w') as f: 
        rad = input('Skriv en rad (tom rad avslutar): ')
        while rad:
            f.write(rad + '\n')
            rad = input('Skriv en rad (tom rad avslutar): ')   
        f.close()
except PermissionError:
   print('Fel - Kunde inte öppna fil. Antingen är den skrivskyddad eller öppnad med ett annat program.')

# Sedan vi stängt filen öppnar vi den på nytt för läsning och visar innehållet
#med en while-loop
try: 
    # existerar inte filen får vi ett felmeddelande
    with open('./test.txt', 'r') as f:
        filinnehåll = f.read()
        f.seek(0,2)
        storlek = f.tell()

except FileNotFoundError:
    print('Fel - hittar inte filen som ska öppnas.')
else:
    print(filinnehåll)
    print('Filens storlek i bytes:',storlek)    
    f.close()
