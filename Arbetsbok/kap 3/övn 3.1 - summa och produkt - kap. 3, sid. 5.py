#!/usr/bin/python3.8

# Filnamn: övn 3.1 - summa och produkt - kap 3, sid. 5.py

# Skapa program eller skript
# Programmeringsövningar till kapitel 3 - Arbetsbok

# Programmet frågar efter två tal och skriver sedan ut vilka talen är,
# vad talens summa är och vad deras produkt är.

# Skriv ut programmets rubrik
print('Summa och produkt')
print('=================\n')

# Fråga efter två tal som också omvandlas från sträng till float (decimaltal)
tal1 = float(input('Ange tal1: '))
tal2 = float(input('Ange tal2: '))


# Beräkna summan av de två angivna talen
summa = tal1 + tal2

# Beräkna produkten av de två angivna talen
produkt = tal1 * tal2

# Skriv ut vilka två tal som matades in tidigare
print('Du matade in följande två tal: ' + str(tal1) + ' och ' + str(tal2) +'.')

# Skriv ut summan av de bägge talen
print('Summan av de bägge talen blev: ' + str(summa) + '.')

# Skriv ut summan av de bägge talen
print('Produkten av de bägge talen blev: ' + str(produkt) + '.')