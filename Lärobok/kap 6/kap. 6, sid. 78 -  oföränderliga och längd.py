#!/usr/bin/python3.8

# Filnamn: kap. 6, sid. 78 -  oföränderliga och längd.py

# Kapitel 6 - Mer om teckensträngar i Python
# Programmering 1 med Python - Lärobok

# Strängar i Python är oföränderliga, ta bort kommentarstecknet # på rad 10
name = 'Hanna'
# name[0] = 'S' # I vissa språk är detta tilåtet och Strängen får en helt 
# annan  innebörd, dvs. Sanna. I Python har man av säkerhetsskäl gjort det 
# omöjligt och följande fel genereras:
# TypeError: 'str' object does not support item assignment

# Längden av en sträng
string = input('Skriv litegrann: ')
lgd = len(string)
print('Du skrev in {0:d} tecken'.format(lgd))

# Skriva ut strängen baklänges med hjälp av len() och index
string = input('Skriv litegrann: ')
length = len(string)
c = length - 1     # För att få sista tecknets indexnr
print('Och baklänges blir det: ')
while c >= 0:
    print(string[c], end = '')
    c -= 1
