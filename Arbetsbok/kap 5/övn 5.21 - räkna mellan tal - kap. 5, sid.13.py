#!/usr/bin/python3.8

# Filnamn: övn 5.21 - räkna mellan tal - kap. 5, sid.13.py

# Programmet frågar efter två tal och räknar upp talen mellan dem.
# Beroende på om första talet är större eller mindre än andra talet så räknar 
# den nedåt eller uppåt. 

steg = 0    # Används för att ange om vi ska räkna uppåt eller nedåt.

# Låt användaren ange två heltal
tal1 = int(input('Ange första talet: '))
tal2 = int(input('Ange andra talet: '))

# Om tal1 är större än tal2 såska vi räkna nedåt och för att få med tal2 i 
# utskriften så måste vi minska det med 1
if tal1 > tal2:
    steg = -1
    tal2 -= 1
else:
# Om tal1 är mindre än tal2 såska vi räkna uppåt och för att få med tal2 i 
# utskriften så måste vi öka det med med 1 (se avsnitt om for-loopen)
    steg = 1
    tal2 += 1

# Skriv ut talen mellan intervallet tal1 -> tal2, med mellanrum mellan varje tal
for i in range(tal1, tal2, steg):
    print(i, end = ' ')

print('')