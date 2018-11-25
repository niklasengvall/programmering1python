#!/usr/bin/python3

# Filnamn: while-loopar, for-loop istället, exempel 4, kap. 5, sid. 66.py

# Programmet skriver ut talen 1 - 20
# och deras kvadrater. Vi använder 
# styrkoden \t för att få utskriften i kolumner

print('Kvadrattabell')
print('=============')
print('Tal\tKvadrat')

#
# i = 1
# while i <= 20:
#     print(i, '\t', i*i)  
#     i += 1

# Har du ett bestämt intervall och inte behöver villkorskontrollera loopen
# är det oftast snabbare och bättre att använda for-loopen.
for i in range(1, 21):
    print(i, '\t', i*i)