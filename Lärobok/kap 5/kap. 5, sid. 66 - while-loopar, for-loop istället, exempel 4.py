#!/usr/local/bin/python3.9

# Filnamn: kap. 5, sid. 66 - while-loopar, for-loop istället, exempel 4.py

# Kapitel 5 - Loopar - upprepning, itteration
# Programmering 1 med Python - Lärobok

# Programmet skriver ut talen 1 - 20
# och deras kvadrater. Vi använder 
# styrkoden \t för att få utskriften i kolumner

print('Kvadreringstabell')
print('=================')
print('Tal\tKvadrat')

# k = 20
# while k <= 40:
#    print(k, '\t', k*k)  
#    k += 1

# Har du ett bestämt intervall och inte behöver villkorskontrollera loopen
# är det oftast snabbare och bättre att använda for-loopen.
for k in range(20, 41):
    print(k, '\t', k*k)