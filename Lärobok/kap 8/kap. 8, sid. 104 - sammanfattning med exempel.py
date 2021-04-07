#!/usr/local/bin/python3.9

# Filnamn: kap. 8, sid. 104 - sammanfattning med exempel.py

# Kapitel 8 - Listor och tipplar
# Programmering 1 med Python - Lärobok

# Exempeldata
lista = [7, 21, 3, 12]
listaLäggTill = [35, 42]
listaSortera = [6, 2, 9, 1]
listaNamn = ['Kalle', 'Ada', 'Pelle', 'Lisa']
# len(x) Ta reda på antal element i en lista samt vilket nr sista index är
antalElement = len(lista)
sistaIndex = antalElement - 1
print('lista: ', lista, 'består av', antalElement, ' element och sista indexposten är',sistaIndex)

# sorted() Skapar en ny lista som är sorterad
print('listaSortera:', listaSortera)
nySorteradLista = sorted(listaSortera)
print('nySorteradLista baserad på en sorterad listaSortera:', nySorteradLista)

# sort() returnerar en sorterad lista 
print('En numrerad lista för sortering:', lista)
lista.sort()
print('En numrerad lista efter sortering:', lista)
print('En alfabetisk lista för sortering:', listaNamn)
listaNamn.sort()
print('En alfabetisk lista efter sortering:', listaNamn)

# append(x) lägg till element i slutet av befintlig lista
print('lista före tillägg:', lista)
lista.append(28)
print('lista efter tillägg:', lista)

# extend(lista) sammanfoga/konkatenera två listor, går med +
print('lista före sammanfogning:', lista)
print('med listaLäggTill:', listaLäggTill)
# lista.extend(listaLäggTill) ¤ Krånglig metod
lista = lista + listaLäggTill # Bättre och enklare metod
print('lista efter sammanfogning:', lista)

# insert(x) infoga elemet på indexposition x
print('listaNamn före infogandet av ett namn till:', listaNamn)
listaNamn.insert(1, 'Agnes')
print('listaNamn efter infogandet av ett namn till:', listaNamn)

# remove(x) tar bort första elementet i en lista med värdet/strängen x
print('listaNamn före borttagande av namnet Kalle:', listaNamn)
listaNamn.remove('Kalle')
print('listaNamn efter borttagande av namnet Kalle:', listaNamn)

# pop(x) ta bort element med index x, utelämnas x tas sista elemnt bort
print('lista före borttag av index 0 och sista index:', lista)
lista.pop(0)
lista.pop()
print('lista efter bottag av index 0 och sista index:', lista)

# index(x) tar reda på index nummer för element x
print('listaNamn:', listaNamn)
finnsPåIndex = listaNamn.index('Lisa')
print('Lisa finns på indexposition:', finnsPåIndex)

# count(x) räkna antal förekomster av element x
lista.append(7) # Vi lägger till en 7:a till lista 
antal7or = lista.count(7)
print('lista ser nu ut så här:', lista)
print('Det finns', antal7or, 'st 7:or i lista')

# reversed() Vänder listan bak och fram
print('lista ser nu ut så här:', lista)
lista.reverse()
print('efter att vi vänt på listan så ser den ut så här:', lista)

