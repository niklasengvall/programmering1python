#!/usr/bin/python3.8

# Filnamn: kap. 8, sid. 97 - loopa genom listor mm.py

# Kapitel 8 - Listor och tipplar
# Programmering 1 med Python - Lärobok

# Använda for- och while-loopar för att gå igenom listors element
enLista = [9, 17, 24, 31, 42, 56]

for c in enLista:
    print(c, end = ' ')

print()

# Skriv ut listan baklänges
c = len(enLista) - 1 # för att få nummret till sista indexpositionen i listan
while c >= 0:
    print(enLista[c], end = ' ')
    c -= 1

print()

# Skapa listor från t.ex. en sträng eller andra iterarbara datatyper
enStr = 'Tage'
enTippel = ('Pelle', 2, 'Stina', 7, 'Kalle', 5)

nyLista1 = list(enStr)
nyLista2 = list(enTippel)

print(nyLista1)
print(nyLista2)

# Mata in data till en nollställd lista 
lista = [] # Nollställd lista
for x in range(1,4): # Låt användaren mata in tre heltal
    lista.append(int(input('Mata in heltal nr ' + str(x) + ':  ')))

print('Dina inmatade tal: ')
for x in lista:
    print(x, end = ', ')

print()