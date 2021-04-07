#!/usr/local/bin/python3.9

# Filnamn: övn 3.2 - areaberäkning av en triangel - kap 3, sid. 5.py

# Skapa program eller skript
# Programmeringsövningar till kapitel 3 - Arbetsbok

# Programmet frågar efter basen och höjden i en triangel. Sedan beräknas arean
# och resultatet skrivs ut på skärmen

# Skriv ut programmets rubrik
print('Beräkna arean på en triangel')
print('============================\n')

# Fråga efter triangelns bas och höjd och omvandla dem från sträng till decimaltal
bas = float(input('Ange triangelns bas: '))
hojd = float(input('Ange triangelns höjd: '))


# Beräkna arean av de två angivna talen
area = bas * hojd / 2

# Skriv ut triangels area på skärmen
print('Triangelns area blir: ' + str(area))

