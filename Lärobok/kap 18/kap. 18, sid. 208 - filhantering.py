#!/usr/bin/python3.8

# Filnamn: kap. kap. 18, sid. 208 - filhantering.py

# Kapitel 19 - Filhantering
# Programmering 1 med Python - Lärobok

# Kodexempel från boken med förklaringar

# Enkelt programexempel som visar skrivning och läsning av
# en textfil. Först öppnar vi filen för skrivning och
# skriver dit något

# öppnar filen, om inte finns skapar den, w = skriver och ersätter tidigare innehåll
try:
    # är filen skrivskyddad eller öppnad av annat program
    f = open('./test.txt', 'w') 
except:   
    print('Fel - kunde inte öppna fil. Antingen är den skrivskyddad eller öppnad med ett annat program.')
else:
    rad = input('Skriv en rad (tom rad avslutar): ')
    while rad:
        f.write(rad + '\n')
        rad = input('Skriv en rad (tom rad avslutar): ')   
    f.close()

# Sedan vi stängt filen öppnar vi den på nytt för läsning och visar innehållet

# antingen med en while-loop
try: 
    # existerar inte filen får vi ett felmeddelande
    f = open('./test.txt', 'r')
except:
    print('Fel - kunde inte öppna fil.')
else:
    rad = f.readline()
    while rad:
        print(rad, end='')
        rad = f.readline()
    f.close()

# eller med en for-in-loop
f = open('./test.txt', 'r')
for rad in f:
    print(rad, end='')
    rad = f.readline()
f.close()
