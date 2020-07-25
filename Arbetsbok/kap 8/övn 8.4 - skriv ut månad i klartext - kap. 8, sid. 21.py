#!/usr/bin/python3.8

# Filnamn: övn 8.4 - skriv ut månad i klartext - kap. 8, sid. 21.py

# Listor och tipplar
# Programmeringsövningar till kapitel 8

# Programmet frågar efter månadsnummer och skriver därefter ut det i klartext

# Lista med alla månader
månad = ['Januari',
         'Februari',
         'Mars',
         'April',
         'Maj',
         'Juni',
         'Juli',
         'Augusti',
         'September',
         'Oktober',
         'November',
         'December']
        
# Fråga användaren efter månadsnummer
månadNr = int(input('Ange månadsnummer: '))

# Gör en test om användaren matat in felaktigt månadsnummer så ska vi informera 
# om det och fråga användaren efter ett nytt månadsnummer
while månadNr < 1 or månadNr > 12:
    print('Fel: Angivet månadsnummer är utanför intervallet 1 - 12, försök igen!')
    månadNr = int(input('Ange månadsnummer: '))

print('Angivet månadsnummer: ' + str(månadNr) + ', motsvarar månad: ' + månad[månadNr - 1])