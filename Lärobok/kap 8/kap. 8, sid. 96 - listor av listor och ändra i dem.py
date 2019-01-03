#!/usr/bin/python3.7

# Filnamn: kap. 8, sid. 96 - listor av listor och ändra i dem.py

# Kapitel 8 - Listor och tipplar
# Programmering 1 med Python - Lärobok

# Listor av listor, exmpel på en två dimensionell lista
# I Python får raderna vaa olika långa 
lista = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9],
         ['A', 'B', 'C', 'D', 'E', 'F']]

print(lista[0])
print(lista[2])
print(lista[2][2])
print(lista[3][5])

# Ändra element
min_lista = [15, 22, 7, 18, 33]
min_lista[3] = 56
print(min_lista)

# För att lägga till och ta bort element i slutet av en lista så kan man 
# använda metoderna .append() och pop()
min_lista.append(34) # Lägg till talet 14 i slutet av listan
print(min_lista)
min_lista.pop() # Ta bort sista elemenet
print(min_lista)

# Man kan också infoga respektive ta bort element från önskad indexposition
min_lista.insert(1, 7) # Infoga värdet 5 på indexposition 1
print(min_lista)
min_lista.pop(4) # Ta bort värdet 34 som nu finns på indexposition 4
print(min_lista)