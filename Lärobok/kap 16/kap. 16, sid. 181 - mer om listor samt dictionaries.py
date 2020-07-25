#!/usr/local/bin/python3.8

# Filnamn: kap. 16, sid. 181 - mer om listor samt dictionaries.py

# Kapitel 16 - Mer om listor samt dictionaries
# Programmering 1 med Python - Lärobok

# Kodexempel från boken med förklaringar

# Så kallade slices med listor, strängar och tippler
#  index   012345678
vokaler = "aeiouyåäö"
# Kom ihåg att sista index ej räknas, i exemplet nedan 9, precis som i range
print(vokaler[6:9])
primtal = (1, 3, 5, 7, 11)
print(primtal[1:4])
tärning = [1, 2, 3, 4, 5, 6]
print(tärning[0:3])

namn = "Tage Test"
# Första index antas vara 0
print(namn[:4])
# Utelämnas sista index tas alla element med 
print(namn[5:])
# negativt startindex tas listan, tippeln eller strängen med baklänges med x 
# antal tecken 
print(namn[-4:])

# Omvandla strängar och tipplar till listor
förnamnStr = "Ture"
förnamnLst = list(förnamnStr)
print(förnamnStr, förnamnLst)
uddaTpl = (1, 3, 5, 7, 9)
uddaLst = list(uddaTpl)
print(uddaTpl, uddaLst)

# Strängmetoden split delar upp en sträng i olika list-bitar
fras = "Solen skiner idag"
# Dela utpp frasen där det finns mellanslag
nyfras = fras.split(' ')
print(fras, nyfras)
