#!/usr/local/bin/python3.9

# Filnamn: kap. 16, sid. 186 - loopa, sortera på nycklar eller value.py

# Kapitel 16 - Mer om listor samt dictionaries
# Programmering 1 med Python - Lärobok

# Kodexempel från boken med förklaringar

# Skapa en associativ array (dictionary) med namn som nycklar och anknytningsnr 
# som värde
anknytning = {'Eva':4530, 'Ola':4839, 'Niklas':6386, 'Agnes':4823}

# Skriv ut alla nycklar och värden med metoden items()
print(anknytning.items())
for nyckel, ankn in anknytning.items():
    print(nyckel,'har anknytning', ankn)

# Skriv ut alla nycklar
print(anknytning.keys())
# Skriv ut alla nycklar sorterade (men de sorteras inte i verkligheten)
print(sorted(anknytning.keys()))
# Skriv ut hela dictionary sorterad på keys()
for nyckel in sorted(anknytning.keys()):
    print(nyckel,'=', anknytning[nyckel])

# Skriv ut alla värden
print(anknytning.values())
# Skriv ut alla värden sorterade (men de sorteras inte i verkligheten)
print(sorted(anknytning.values()))
# Skriv ut hela dictionary sorterad på värden()
for värde in sorted(anknytning.values()):
    print(värde, end=', ')

print()
# nycklar och värden måste inte vara i ordningen stängar och tal
sexansTabell = {1: 6, 2: 12, 3: 18, 4: 24, 5: 30}
for i, tal in sexansTabell.items():
    print(i,'*', '6 =', tal)
sifferOrd = {1: 'ett', 2: 'två', 3: 'tre', 4: 'fyra', 5: 'fem', 6: 'sex'}
for siffra, Ord in sifferOrd.items():
    print('Siffran', siffra, 'skrivs med ord som', Ord)

