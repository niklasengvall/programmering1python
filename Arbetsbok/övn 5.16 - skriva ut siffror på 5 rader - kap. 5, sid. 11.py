#!/usr/bin/python3

# Filnamn: övn 5.16 - skriva ut siffror på 5 rader - kap. 5, sid. 11.py

# Programmet skriver ut siffrorna 1 till 9 på 5 rader med mellanrum mellan 
# varje siffra och radslutstecken i slutet på varje rad 

for y in range(5):
    for x in range(1, 10):
        print(x, end = ' ')
    print('')
