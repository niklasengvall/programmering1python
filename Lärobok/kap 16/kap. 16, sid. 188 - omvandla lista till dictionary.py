#!/usr/local/bin/python3.8

# Filnamn: kap. 16, sid. 188 - omvandla lista till dictionary.py

# Kapitel 16 - Mer om listor samt dictionaries
# Programmering 1 med Python - Lärobok

# Kodexempel från boken med förklaringar

# Skapa en lista av tipplar
anknLT = [('Agnes', 4823), ('Eva', 4530), ('Niklas', 6386), ('Ola', 4839)]
# Skapa en lista av listor
anknLL = [['Eva', 4530], ['Agnes', 4823], ['Ola', 4839], ['Niklas', 6386]]

# Skriver ut listorna innan konvertering till dictionaries
print('', anknLT)
print('', anknLL)

# Skapa två dictionaries baserade på de två listorna
anknDLT = dict(anknLT)
anknDLL = dict(anknLL)

# SKriv ut de två nya dictionaries
print('Dictionaryn anknDLT:', anknDLT)
print('Dictionaryn anknDLL:', anknDLL)
