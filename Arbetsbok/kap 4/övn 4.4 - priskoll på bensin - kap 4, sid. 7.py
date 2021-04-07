#!/usr/local/bin/python3.9

# Filnamn: övn 4.4 - priskoll på bensin - kap 4, sid. 7.py

# Skapa program eller skript
# Programmeringsövningar till kapitel 4 - Arbetsbok

# Programmet frågar efter bensinpris och som sedan med villkor talar om
# om det är billigt eller inte.

# Skriv ut programmets rubrik
print('Priskoll på bensin')
print('==================\n')

# Fråga efter bensinpriset och omvandla siffrorna från sträng till decimaltal
bensinPris = float(input('Vad kostar bensinen per liter: '))

# Utifrån bensinpriset, testa med villkor och berätta för användaren om det är
# billigt eller dyrt 
if bensinPris > 20:
    print('Nu säljer jag bilen och cyklar istället')
elif bensinPris > 15:
    print('Tanka tio liter')
elif bensinPris > 10:
    print('Tanka full tank')
else:
    print('Det var billigt')
