#!/usr/bin/python3

# Filnamn: övn 4.2 - beräkna BMI med villkor - kap 4, sid. 7.py

# Villkor, IF-satser
# Programmeringsövningar till kapitel 4 - Arbetsbok

# Programmet beräknar och skriver ut BMI (Body Mass Index) och om det är undervikt,
# normalvikt, övervikt eller fetma

# Skriv ut programmets rubrik
print('Beräkna BMI')
print('===========\n')

# Fråga efter kroppsvikt i kilo och längd i meter
# och omvandla siffrorna från sträng till decimaltal
vikt = float(input('Ange din vikt i kilo: '))
längd = float(input('Ange din längd i meter: '))

# Beräkna BMI
bmi = vikt / (längd * längd)

# Skriv ut BMI värdet med en decimal
print('Ditt BMI-värde är: {:.1f}'.format(bmi))

# Berätta om det är undervikt, normalvikt, övervikt eller fetma
if bmi >= 30:
    print('Du har tyvärr fetma.')
elif bmi >= 25:
    print('Du har övervikt.')
elif bmi >= 18.5:
    print('Du har normalvikt.')
else:
    print('Du har undervikt.')
