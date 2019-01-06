#!/usr/bin/python3.7

# Filnamn: kap. kap. 8, sid. 103 - list comprehensions.py

# Kapitel 8 - Listor och tipplar
# Programmering 1 med Python - Lärobok

# Exempeldata
listaEtt = [9, 3, 7]

# Med listomfattningar (list comprehensions) menas att man skapar en ny lista 
# där varje element är resultatet av någon operation på en annan 
# itererbar variabel eventuella villkor måste också uppfyllas

# Här skapar vi en ny lista med uppräkning av t, talen finns ej från början
listaTvå = [t for t in range(10)]
print(listaTvå)

# Skapar en ny lista med utgångspunkt av t i range-inställningarna
listaTre = [t for t in range(3, 10, 3)]
print('listaTre:', listaTre)

# Skapar en ny lista med utgångspunkt av att kvadrera t utifrån
# range-inställningarna
listaFyra = [t**2 for t in range(3, 10, 3)]
print('listaFyra:', listaFyra)

# Skapa en ny lista där villkoret att inte ta med tal som är jämt delbara med 5
listaFem = [t for t in range(1, 26) if t % 5 != 0]
print('listaFem:', listaFem)

# Slå samman listor (konkatenera)
listaEtt = listaEtt + listaFyra
print('Efter sammanslagning med listaFyra är listaEtt:', listaEtt)

# Med metoden append så skapar du en lista i en lista
listaEtt.append(listaTre)
print('Efter sammanslagning med listaTre är listaEtt:', listaEtt)