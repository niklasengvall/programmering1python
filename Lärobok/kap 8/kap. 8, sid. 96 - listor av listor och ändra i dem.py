#!/usr/local/bin/python3.9

# Filnamn: kap. 8, sid. 96 - listor av listor och ändra i dem.py

# Kapitel 8 - Listor och tipplar
# Programmering 1 med Python - Lärobok

# Listor av listor, exmpel på en två dimensionell lista
# I Python får raderna vaa olika långa 
l = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9],
     ['A', 'B', 'C', 'D', 'E', 'F']]

print(l[0])
print(l[2])
print(l[2][2])
print(l[3][5])

# Ändra element
enLista = [15, 22, 7, 18, 33]
enLista[3] = 56
print(enLista)

# För att lägga till och ta bort element i slutet av en lista så kan man 
# använda metoderna .append() och pop()
enLista.append(34) # Lägg till talet 14 i slutet av listann
print(enLista)
enLista.pop() # Ta bort sista elemenet
print(enLista)

# Man kan också infoga respektive ta bort element från önskad indexposition
enLista.insert(1, 7) # Infoga värdet 5 på indexposition 1
print(enLista)
enLista.pop(4) # Ta bort värdet 34 som nu finns på indexposition 4
print(enLista)