#!/usr/bin/python3.7

# Filnamn: övn 5.18 - skriva ut 10 rader med siffror - kap. 5, sid. 11.py

# Programmet skriver ut 10 rader med siffror. Första raden innehåller 10 nollor,
# andra raden 10 siffran ett osv. Det är mellanrum bellan varje siffra och 
# radslutstecken i slutet på varje rad. 

for y in range(10):     # Betyder att vi ska skriva ut 10 rader
    
    for x in range(10): # Betyder att vi ska skriva ut 10 st av var. y innehåll
        print(y, end = ' ')
    
    # radslutstecken
    print('')
