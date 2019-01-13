#!/usr/bin/python3.7

# Filnamn: övn 8.2 - skriv ut i omvänd ordning - kap. 8, sid. 21.py

# Listor och tipplar
# Programmeringsövningar till kapitel 8

# Programmet frågar efter hur många tal du vill mata in, låter dig sedan mata 
# in dessa en i taget. Efter varje inmatning läggs det inmatade talet till 
# listan. Slutligen loopar programmet igenom listan i omvänd ordning och 
# skriver ut varje tal. 
listaTal = [] # Tom lista som lagrar antTal element innehållande tal

# Fråga användaren hur många tal som ska matas in
antTal = int(input('Hur många tal vill du mata in? '))

# Be användaren mata in antTal st tal och lagra dem som varsit nytt element i 
# listan listaTal
for i in range(antTal):
    listaTal.append(float(input('Ange tal ' + str(i+1) + ': ')))

# Skriv ut talen i den omvänd ordning, dvs sista inmatade till första ifrån
# listan listaTal
for i in range(antTal - 1 , -1, -1):
    print('Tal ' + str(i + 1) + ': ' + str(listaTal[i]))