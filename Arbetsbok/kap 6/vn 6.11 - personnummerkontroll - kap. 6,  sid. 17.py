#!/usr/bin/python3.7

# Filnamn: övn 6.11 - personnummerkontroll - kap. 6,  sid. 17.py

# Mer om teckensträngar i Python
# Programmeringsövningar till kapitel 6

# Programmet kontrollerar om inmatat personnummer är ok

# Låt användaren mata in en ett personummer
personnr = str(input('Ange ett personnummer: '))

# Kontrollera om 11 tecken och '-' matats in
if len(personnr) == 11 and '-' in personnr:
    personnr = personnr.replace('-', '')

# Om det inte är 10 siffror angivna, avbryt och meddela användaren
if len(personnr) != 10:
    print('Ogiltigt personnummer angivet! Det saknas ' + str(10 - len(personnr)) + ' siffra/siffror')
    exit()

sum = 0
# Räkna ut kontrollsiffra
# Udda siffror multipliceras med 2, blir resultatet större än 9, minska med 9
# Summera alla produkter
for i in range(0, 10, 2):
    if (int(personnr[i]) * 2) > 9:
        sum += (int(personnr[i]) * 2) - 9
    else:
        sum += (int(personnr[i]) * 2)

# Summera sedan alla jämna siffror
for i in range(1, 10, 2):
    sum += int(personnr[i])

# Om kontrollsiffran är jämt delbar med 10 så är det ok
if sum % 10:
    print('Angivet personnummer är felaktigt: Kontrollsifran stämmer ej!')
else: 
    print('Angivet personnummer är OK!')