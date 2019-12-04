#!/usr/bin/python3.7

# Filnamn: kap. 8, sid. 102 - kopior och listomfattningar.py

# Kapitel 8 - Listor och tipplar
# Programmering 1 med Python - Lärobok

# Exempeldata
listaEtt = [9,3,7]
lista2d = [[0, 0, 0],
           [0, 0, 1],
           [0, 1, 0],
           [0, 1, 1],
           [1, 0, 0],
           [1, 0, 1],
           [1, 1, 0],
           [1, 1, 1]]
# Olika metoder för att kopiera en lista
# Import av kopieringsmodul och använda metoden copy samt deepcopy
import copy
# copy för att kopiera endimensionella listor
listaTvå = copy.copy(listaEtt)
print('listaEtt', listaEtt)
print('listaTvå', listaTvå)

# Skriv ut id för bägge variablerna, olikanr => olika objekt
print(id(listaEtt), id(listaTvå))
listaEtt[2] = 8
listaTvå[0] = 6

# Skriv ut det nya innehållet
print(listaEtt)
print(listaTvå)

# visa vad som händer när man kör copy på en flerdimensionell lista
listaTre = copy.copy(lista2d)
print('lista2d', lista2d)
print('listaTre', listaTre)

# Skriv ut id för bägge variablerna, olikanr => olika objekt
# Men de hänvisar i dimension 2 till samma minnesområde
print(id(lista2d), id(listaTre))
lista2d[0][2] = 2
listaTre[0][0] = 2
print(lista2d)
print(listaTre)

# deepcopy för att kopiera flerdimensionella listor
# Nu kommer dimension två att bli olika värden
listaFyra = copy.deepcopy(lista2d)
print('lista2d', listaEtt)
print('listaFyra', listaFyra)

# Skriv ut id för bägge variablerna, olikanr => olika objekt
print(id(lista2d), id(listaFyra))
lista2d[0][2] = 0
listaFyra[0][0] = 0

print(lista2d)
print(listaFyra)

# Enklaste sättet föratt kopiera listor är med slice

listaTvå = listaEtt[:]
print(id(listaEtt), id(listaTvå))
print('listaEtt', listaEtt)
print('listaTvå', listaTvå)