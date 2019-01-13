#!/usr/bin/python3.7

# Filnamn: övn 8.3 - beräkna summa och medelvärde av lista - kap. 8, sid. 21.py

# Listor och tipplar
# Programmeringsövningar till kapitel 8

# Programmet frågar efter hur många tal du vill mata in, låter dig sedan mata 
# in dessa en i taget. Efter varje inmatning läggs det inmatade talet till 
# listan. Därefter beräknar programmet summan och medelvärdet av listans tal. 
# Slutligen skrivs listans summa och medelvärdet ut på konsolen
listaTal = [] # Tom lista som lagrar antTal element innehållande tal

# Fråga användaren hur många tal som ska matas in
antTal = int(input('Hur många tal vill du mata in? '))

# Be användaren mata in antTal st tal och lagra dem som varsit nytt element i 
# listan listaTal
for i in range(antTal):
    listaTal.append(float(input('Ange tal ' + str(i+1) + ': ')))

# Beräkna summan av alla inmatade tal 
summa = 0 # Måste inieras denna annars tror systemet att summa också är en lista
for i in range(antTal):
    summa += listaTal[i] # Här är det viktigt att summa initierats innan

# Beräkna medelvärdet av listan alla tal
medel = summa / antTal
# Skriv ut summan och medelvärdet på konsolen    
print('Summan av alla inmatade tal blev ' + str(summa) + ' och medelvärdet blev ' + str(medel))