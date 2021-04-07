#!/usr/local/bin/python3.9

# Filnamn: exempel från svar till testa dig själv fråga 11.py

# Kapitel 18 - Filhantering 
# Programmering 1 med Python - Lärobok

# Skriver ut innehållet från en textfils första rad
fil = open('test2.txt', 'r', encoding = 'utf-8')
rad = fil.readline()
fil.close()
print(rad, end = '') # Skriver ut raden på konsolen

# Skriver ut innehållet från en textfil rad för rad
fil = open('test2.txt', 'r', encoding = 'utf-8')
rader = fil.readlines()
fil.close()
for rad in rader:
    print(rad.strip()) # Skriver ut en rad i taget på konsolen

# Skriv ut allt textinnehåll på engång 
fil = open('test2.txt', 'r', encoding = 'utf-8')
texten = fil.read()
fil.close()
print(texten) # Skriver ut alla rader på konsolen