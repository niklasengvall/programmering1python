#!/usr/bin/python3

# Filnamn: övn 4.1 - beräkna medelvärde på prov - kap 4, sid. 7.py

# Villkor, IF-satser
# Programmeringsövningar till kapitel 4 - Arbetsbok

# Programmet frågar efter poäng på 3 olika prov, beräknar därefter medelvärdet
# och skriver ut det. Om medelvärdet är över 90 så skriver programmet också ut 
# "Bra jobbat!"

# Skriv ut programmets rubrik
print('Beräkna medelvärde med villkor')
print('==============================\n')

# Fråga efter tre olika provresultat
# och omvandla siffrorna från sträng till decimaltal
prov1 = float(input('Ange poäng på prov 1: '))
prov2 = float(input('Ange poäng på prov 2: '))
prov3 = float(input('Ange poäng på prov 3: '))

# Beräkna medelvärdet för de tre angivna proven
medel = (prov1 + prov2 + prov3) / 3

# Skriv ut medelvärdet och är det dessutom över 90 poäng,
# skriver programmet ut att det är "Bra jobbat"
print('Medelvärdet för de tre proven blev: ' + str(medel) + ' poäng.')
if medel > 90:
    print('\"Bra jobbat!\"')
