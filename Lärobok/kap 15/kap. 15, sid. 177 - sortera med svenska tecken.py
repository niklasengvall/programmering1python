#!/usr/local/bin/python3.7

# Filnamn: kap. 15, sid. 177 - sortera med svenska tecken.py

# Kapitel 15 - Sorteringar
# Programmering 1 med Python - Lärobok

# Kodexempel från boken med förklaringar

# Översättningstabell för att jämföra svenska strängar
svTabell = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖåäöéÉàÀüÜ',
                         'abcdefghijklmnopqrstuvwxyz{|}{|}eeaayy')
def jämför(sträng):
    return sträng.translate(svTabell)

efternamn = ['Åberg', 'Öberg', 'Viklund', 'andersson', 'Arnberg', 'Ärlandsson',              'Sträng', 'Ottosson', 'Engvall']

# Skriver ut en nyskapad sorterad lista
print(sorted(efternamn, key=jämför))
# Skriver ut en befintlig sorterad lista
efternamn.sort(key=jämför)
print(efternamn)

