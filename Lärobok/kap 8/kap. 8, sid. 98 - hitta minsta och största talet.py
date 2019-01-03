#!/usr/bin/python3.7

# Filnamn: kap. 8, sid. 98 - hitta minsta och största talet.py

# Kapitel 8 - Listor och tipplar
# Programmering 1 med Python - Lärobok

# Två sätt för att hitta minsta repektive största talet i en lista

# Listan vi ska söka igenom
num = [17, 9, 24, 56, 42, 31]

# Utgå ifrån att minsta respektive största talet finns på indexposition 0
m = num[0] # Minsta talet
s = num[0] # Största talet

# Gå igenom alla talen, vanligt i c/c++, c#, java och javascript
for c in num:
    # Om vi hittar ett mindre tal senare i listan spara det som det minsta talet
    if c < m:
        m = c
    # Om vi hittar ett större tal senare i listan spara det som det minsta talet
    if c > s:
        s = c
# SKriv ut minsta respektiv största talet
print('I listan så är minsta talet ' + str(m) + ' och största talet är ' + str(s) + '.')

# Pythons inbyggda funktioner för att hitta minsta resp. största tal i en lista
print('Pythons inbyggda funktioner säger att minsta talet är ' + str(min(num)) + ' och största talet är ' +  str(max(num)) + '.')