#!/usr/bin/python3.7

# Filnamn: övn 4.5 - skottår - kap 4, sid. 7.py

# Skapa program eller skript
# Programmeringsövningar till kapitel 4 - Arbetsbok

# Programmet frågar efter ett årtal och som sedan talar om ifall det är ett
# skottår

# Skriv ut programmets rubrik
print('Skottårs kontroll')
print('=================\n')

# Fråga efter bensinpriset och omvandla siffrorna från sträng till decimaltal
skottÅr = int(input('Ange ett årtal: '))

# Kntrollera omanvändaren anger ett årtal inan den gregorianska kalendern 
# infördes
if skottÅr < 1753:
    print('Skottår fanns inte innan den gregorianska kalendern infördes år 1753')
# Kontrollerar om årtalet är jämt delbart med 4 eller med 400 med modulus
# operatorn ger någon av de noll i retur så är det ett skottår
elif skottÅr % 4 == 0 or skottÅr % 400 == 0: 
    print('År ' + str(skottÅr) + ' är ett skottår!')
else:
    print('År ' + str(skottÅr) + ' är inte ett skottår!')