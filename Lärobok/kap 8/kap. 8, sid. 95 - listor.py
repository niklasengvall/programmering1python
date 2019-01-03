#!/usr/bin/python3.7

# Filnamn: kap. 8, sid. 95 - listor.py

# Kapitel 8 - Listor och tipplar
# Programmering 1 med Python - Lärobok

# Listor är vad man i andra språk kallar vektorer, fält, arrayer 
# eller endimensionella matriser

# En lista är en ordnad samling element som var och en kan identifieras med en 
# siffra, ett index. Element anges inom hakparenteser

tal = [17, 10, 2]
print(tal)
print(tal[0])

tecken = ['Z', '?', 'q', '2']
print(tecken[1])
print(tecken[2])

namn = ['Ada', 'Pascal', 'Bjarne']
print(namn[0])
print(namn[2])

# Precis som med strängar så börjar indexeringen på 0, har man 5 element i en 
# lista så har sista elementet index 4

# Observera att i Python behöver inte elementen ha samma datatyp, det är 
# dynamiskt typat 

q = False
z = 3
lista = [7, 'Nisse', 6.28, z, q]
print(lista[4])
print(lista[1])