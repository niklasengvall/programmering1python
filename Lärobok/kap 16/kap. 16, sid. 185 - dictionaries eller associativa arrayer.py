#!/usr/local/bin/python3.9

# Filnamn: kap. 16, sid. 185 - dictionaries eller associativa arrayer.py

# Kapitel 16 - Mer om listor samt dictionaries
# Programmering 1 med Python - Lärobok

# Kodexempel från boken med förklaringar

# För att få index och listelement samtidigt använder man funktionen enumerate()
# Det är en snabbare metod än att använda den gamla klassiska metoden

# Skapa en associativ array (dictionary) med namn som nycklar och anknytningsnr 
# som värde
anknytning = {'Eva':4530, 'Ola':4839, 'Niklas':6386, 'Agnes':4823}

# Skriv ut hela arrayen
print(anknytning)

# Skriv ut Agnes och Olas anknytningar
print(anknytning['Agnes'],anknytning['Ola'])

# Ändra Niklas anknytning
anknytning['Niklas'] = 4539

# Skriv ut hela arrayen igen
print(anknytning)

# Ta bort nyckeln Eva och skriv ut hela arrayen igen
del(anknytning['Eva'])
print(anknytning)

