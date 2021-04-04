#!/usr/local/bin/python3.9

# name: kap. 8, sid. 95 - listor.py

# Kapitel 8 - Listor och tipplar
# Programmering 1 med Python - Lärobok

# Listor är vad man i andra språk kallar vektorer, fält, arrayer 
# eller endimensionella matriser

# En enLista är en ordnad samling element som var och en kan identifieras med en 
# siffra, ett index. Element anges inom hakparenteser

num = [17, 10, 2]
print(num)
print(num[0])

char = ['Z', '?', 'q', '2']
print(char[1])
print(char[2])

name = ['Ada', 'Pascal', 'Bjarne']
print(name[0])
print(name[2])

# Precis som med strängar så börjar indexeringen på 0, har man 5 element i en 
# lista så har sista elementet index 4

# Observera att i Python behöver inte elementen ha samma datatyp, det är 
# dynamiskt typat 

q = False
z = 3
enLista = [7, 'Nisse', 6.28, z, q]
print(enLista[4])
print(enLista[1])