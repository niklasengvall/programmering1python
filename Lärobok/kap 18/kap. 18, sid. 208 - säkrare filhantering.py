#!/usr/bin/python3.8

# Filnamn: kap. 18, sid. 208 - säkrare filhantering.py

# Kapitel 19 - Filhantering
# Programmering 1 med Python - Lärobok

# Kodexempel från boken med förklaringar

# Enkelt programexempel som visar skrivning och läsning av
# en textfil. Först öppnar vi filen för skrivning och
# skriver dit något

# öppnar filen med en säkrare sk kontex öppning, om inte filen 
# finns skapas den, w = skriver och ersätter tidigare innehåll
try:
    # ./ skapar filen test.txt en nivå högre upp i filhierarkin
    with open('./test.txt', 'w', encoding = 'utf-8') as f:
        rad = input('Skriv en rad (tom rad avslutar): ')
        while rad:
            f.write(rad + '\n')
            rad = input('Skriv en rad (tom rad avslutar): ')   
        f.close()
# Filen är antingen skrivskyddad eller öppen i ett annat program och systemet kan ej hantera detta utan exklusiv åtkomst
except PermissionError:
   print('Fel - Kunde inte öppna fil. Antingen är den skrivskyddad eller öppnad med ett annat program.')

# Sedan vi stängt filen öppnar vi den på nytt för läsning och visar innehållet
#med en while-loop
try: 
    # Öppna och läs in hela filen    
    with open('./test.txt', 'r', encoding = 'utf-8') as f:
        filinnehåll = f.read()
        # Placera filpekaren med 0 steg från filens slut 2
        f.seek(0,2)
        # Positionen avslöjas med funktionen tell() och står vi i slutet så får vi filstorleken
        storlek = f.tell()

# existerar inte filen får vi ett felmeddelande
except FileNotFoundError:
    print('Fel - hittar inte filen som ska öppnas.')
else:
    print(filinnehåll)
    print('Filens storlek i bytes:',storlek)    
    f.close()
