#!/usr/bin/python3.7

# Filnamn: övn 8.6 - minsta byter plats med första - kap. 8, sid. 21.py

# Listor och tipplar
# Programmeringsövningar till kapitel 8

# Programmet letar efter en listas minsta tal och placerar det som listans 
# första element. Därefter skrivs listan ut som kontroll

# Lista med 15 tal
tal = [23, 89, 3, 63, 12, 34, 42, 97, 51, 67, 7, 18, 24, 91, 72]
        
# Leta efter minsta tal och lagra det samt dess index
minsta = tal[0] # sätt minsta tal till listans första element
for i in range(len(tal)): # Gå igenom alla element i listan
    if tal[i] < minsta: # Finns ett element i listan som är mindre än var minsta
        minsta = tal[i] # Sätt var minsta till det nya mindre elementet  
        indexnr = i     # och lagra dess indexposition

# Skriv ut listan tal före förändring
print('tal före förändring: ', tal)

# Byt plats mellan listans första tal och dess minsta tal 
#temp = tal[0] 
#tal[0] = tal[indexnr]
#tal[indexnr] = temp
# Gör om till tippel och byt plats på värdena
tal[0], tal[indexnr] = tal[indexnr], tal[0]

# Skriv ut listan tal efter förändring
print('tal efter förändring:', tal)
