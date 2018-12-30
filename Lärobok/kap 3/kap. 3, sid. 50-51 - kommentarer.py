#!/usr/bin/python3.7

# Filnamn: kap. 3, sid. 50-51 - kommentarer.py

# Programmering 1 med Python - Lärobok
# Kapitel 3 - Skapa program eller skript

# Kommentarer i program
# Programmet konverterar från Celcius till Fahrenheit

# Inmatning av gradtal i Celciusskalan
celcius = float(input('Ange grader i Celcius: '))

# Omvandling till Fahrenheit
fahrenheit = celcius * 9 / 5 + 32

# Utskrift av resultatet med en decimal
print('Det blir {:.1f} grader fahrenheit'.format(fahrenheit))

# Exempel på onödig kommentar
# x += 1 # Öka x med ett

# Exempel på bra kommentar om vad raden/raderna nedanför har för avsikt
# x += 1 # För att ha viss marginal


