#!/usr/local/bin/python3.9

# Filnamn: kap. 16, sid. 187 - sortera en lista av tipplar eller lista av
# listor.py

# Kapitel 16 - Mer om listor samt dictionaries
# Programmering 1 med Python - Lärobok

# Kodexempel från boken med förklaringar

# Funktioner
# Funktion som tar ett listelement som parameter och returnerar värdet för det 
# index det ska sorteras på
def jmfrNyckel(z):
    return z[0] # sortera på index 0 (nyckeln)

def jmfrAnkn(z):
    return z[1] # sortera på index 1 (värdet)

# Skapa en associativ array (dictionary) med namn som nycklar och anknytningsnr 
# som värde

anknytning = {'Eva':4530, 'Ola':4839, 'Niklas':6386, 'Agnes':4823}
# Skriver ut dictionaryn
print('Dictionaryn:', anknytning)

# Skapa en ny lista med tipplar utav dictionaryn och skriv ut den
listaMedTipplar = list(anknytning.items()) 
# Skriver ut listan med tipplar före sortering
print('listaMedTipplar före sortering:', listaMedTipplar)

# Skapa en ny lista av listor utav dictionaryn och skriv ut den
listaMedListor = [[namn, ankn] for namn, ankn in anknytning.items()]
# Skriver ut listan med listor före sortering
print('listaMedListor före sortering:', listaMedListor)

# Sortera listan med tipplar efter nyckel
listaMedTipplar.sort(key=jmfrNyckel)
print('listaMedTipplar efter sortering:',listaMedTipplar)

# Sortera listan med listor efter anknytning
listaMedListor.sort(key=jmfrAnkn)
print('listaMedListor efter sortering:',listaMedListor)
