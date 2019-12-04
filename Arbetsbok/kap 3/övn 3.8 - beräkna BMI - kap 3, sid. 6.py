#!/usr/bin/python3.8

# Filnamn: övn 3.8 - beräkna BMI - kap 3, sid. 6.py

# Skapa program eller skript
# Programmeringsövningar till kapitel 3 - Arbetsbok

# Programmet beräknar och skriver ut BMI (Body Mass Index)

# Skriv ut programmets rubrik
print('Beräkna BMI')
print('===========\n')

# Fråga efter kroppsvikt i kilo och längd i meter
# och omvandla siffrorna från sträng till decimaltal
vikt = float(input('Ange vikt i kilo: '))
längd = float(input('Ange längd i meter: '))

# Beräkna BMI
bmi = vikt / (längd * längd)

# Skriv ut BMI värdet med en decimal
print('BMI för denna person är: {:.1f}'.format(bmi))
