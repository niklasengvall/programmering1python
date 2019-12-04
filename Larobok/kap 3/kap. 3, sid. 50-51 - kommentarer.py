#!/usr/bin/python3.7

# Filnamn: kap. 3, sid. 50-51 - kommentarer.py

# Kapitel 3 - Skapa program eller skript
# Programmering 1 med Python - Lärobok

# Kommentarer i program
# Programmet omvandlar från Celcius till Fahrenheit

# Ta emot inmatning av gradtal i Celcius
c = float(input('Mata in grader i Celcius: '))

# Omvandla till Fahrenheit
f = c * 9 / 5 + 32

# Skriv ut resultatet med två decimalers noggranhet
print('De angivna graderna i Celcius blir {:.2f} grader i fahrenheit'.format(f))

# Exempel på onödig kommentar
# a += 1 # Lägg till ett till a variabeln

# Exempel på bra kommentar om vad raden/raderna nedanför har för avsikt
# a += 2 # För att ha bättre omfång


