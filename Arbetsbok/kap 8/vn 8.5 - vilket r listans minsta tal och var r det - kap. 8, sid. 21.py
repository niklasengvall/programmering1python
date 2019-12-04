#!/usr/bin/python3.7

# Filnamn: övn 8.5 - vilket är listans minsta tal och var är det - kap. 8, sid. 
# 21.py

# Listor och tipplar
# Programmeringsövningar till kapitel 8

# Programmet letar efter en listas minsta tal och skriver sedan ut det och 
# vilket index det har

# Lista med 15 tal
tal = [23, 89, 3, 63, 12, 34, 42, 97, 51, 67, 7, 18, 24, 91, 72]
        
# Leta efter minsta tal och lagra det samt dess index
minsta = tal[0] # sätt minsta tal till listans första element
for i in range(len(tal)): # Gå igenom alla element i listan
    if tal[i] < minsta: # Finns ett element i listan som är mindre än var minsta
        minsta = tal[i] # Sätt var minsta till det nya mindre elementet  
        indexnr = i     # och lagra dess indexposition

# Skriv ut minsta talet och dess index
print('Minsta talet som hittades i listan tal: \n' + str(tal) + ' är ' + str(minsta) + ', och det finns som element i tal[' + str(indexnr) + ']')