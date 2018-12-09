#!/usr/bin/python3

# Filnamn: övn 4.3 - villkor av flera vilkor - kap 4, sid. 7.py

# Villkor, IF-satser
# Programmeringsövningar till kapitel 4 - Arbetsbok

# Programmet beräknar och skriver ut BMI (Body Mass Index) och om det är undervikt,
# normalvikt, övervikt eller fetma

# Skriv ut programmets rubrik
print('Villkor')
print('=======\n')

# Fråga efter tre värden
# och omvandla siffrorna från sträng till heltal
a = int(input('Ange värde för a:  '))
b = int(input('Ange värde för b:  '))
c = int(input('Ange värde för c:  '))

# Testa först om a < b och b < c
if a < b and b < c:
    pass
elif a < b or b < c:  
    print('Antingen är a mindre än b eller b mindre än c')
