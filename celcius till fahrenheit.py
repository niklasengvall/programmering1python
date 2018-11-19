#!/usr/bin/python3                          
# Filnamn: celcius till fahrenheit.py
# Kodexempel, lärobok sid. 50

# Programmet konverterar från Celcius till Fahrenheit

# Inmatning av gradtal i Celciusskalan
celcius = float(input('Ange grader i Celcius: '))

# Omvandling till Fahrenheit
fahrenheit = celcius * 9 / 5 + 32

# Utskrift av resultatet med en decimal
print('Det blir {:.1f} grader fahrenheit'.format(fahrenheit))