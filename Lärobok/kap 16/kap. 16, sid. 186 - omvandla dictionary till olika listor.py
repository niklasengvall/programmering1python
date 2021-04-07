#!/usr/local/bin/python3.9

# Filnamn: kap. 16, sid. 186 - omvandla dictionary till olika listor.py

# Kapitel 16 - Mer om listor samt dictionaries
# Programmering 1 med Python - Lärobok

# Kodexempel från boken med förklaringar

# Skapa en associativ array (dictionary) med namn som nycklar och anknytningsnr 
# som värde
anknytning = {'Eva':4530, 'Ola':4839, 'Niklas':6386, 'Agnes':4823}

# Skriv ut dictionaryn
print(anknytning)

# Skapa en ny lista med tipplar utav dictionaryn och skriv ut den
listaMedTipplar = list(anknytning.items()) 
print(listaMedTipplar)
# Skriv ut tippel 1
print(listaMedTipplar[1])
enTippel = listaMedTipplar[1]
# Skriv ut första indexet i tippeln
print(enTippel[0])

# Skapa en ny lista av listor utav dictionaryn och skriv ut den
listaMedListor = [[namn, ankn] for namn, ankn in anknytning.items()]
print(listaMedListor)
# Skriv ut endast ut ett av namnen i listan
print(listaMedListor[2][0])