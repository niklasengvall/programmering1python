#!/usr/bin/python3.7

# Filnamn: oföränderliga och längd - kap. 6, sid. 78.py

# Programmering 1 med Python - Lärobok
# Kapitel 6 - Mer om teckensträngar i Python

# Strängar i Python är oföränderliga, ta bort kommentarstecknet # på rad 10
namn = 'Hanna'
# namn[0] = 'S' # I vissa språk är detta tilåtet och Strängen får en helt 
# annan  innebörd, dvs. Sanna. I Python har man av säkerhetsskäl gjort det 
# omöjligt och följande fel genereras:
# TypeError: 'str' object does not support item assignment

# Längden av en sträng
s = input('Skriv något: ')
lgd = len(s)
print('Du skrev in {0:d} tecken'.format(lgd))

# Skriva ut strängen baklänges med hjälp av len() och index
s = input('Skriv något: ')
lgd = len(s)
i = lgd - 1     # För att få sista tecknets indexnr
print('Baklänges blir det: ')
while i >= 0:
    print(s[i], end = '')
    i -= 1
