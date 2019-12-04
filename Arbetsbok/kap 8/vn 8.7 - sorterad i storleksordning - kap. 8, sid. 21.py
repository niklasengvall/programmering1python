#!/usr/bin/python3.8

# Filnamn: övn 8.7 - sorterad i storleksordning - kap. 8, sid. 21.py

# Listor och tipplar
# Programmeringsövningar till kapitel 8

# Programmet sorterar en listas element i storleksordning. Därefter skrivs 
# listan ut som kontroll
# lista.sort() skulle lösa detta snabbare och effektivare men nu är det övning

# Lista med 15 tal
tal = [23, 89, 3, 63, 12, 34, 42, 97, 51, 67, 7, 18, 24, 91, 72]
tal2 = tal[:] # Kopiera tal till listan tal2

# Skriv ut listan tal före förändring
print('tal före förändring: ', tal)

# Gå igenom listan element för element, växla plats på element som är mindre 
for i in range(len(tal)): # Gå igenom alla element i listan
    minsta = tal[i]
    index = 0
    bytt = False
    for j in range(i, len(tal)): # inre loop för att jämför mot
        if tal[j] < minsta: # Kontroll om element är större än nästkommande 
            minsta = tal[j]
            index = j
            bytt = True # För att undvika fal

    # Byt plats så mindre tal hamnar mer i början av listan
    if bytt: # Byt endast plats om vi hittat mindre tal
        tal[i], tal[index] = tal[index], tal[i]
        bytt = False

# Skriv ut listan tal efter förändring
print('tal efter förändring:', tal)

# Skriv ut listan tal2 före förändring
print('tal2 före förändring: ', tal2)
# snabb inbyggd sorteringsfunktion
tal2.sort()
# Skriv ut listan tal efter förändring
print('tal2 efter förändring:', tal2)
