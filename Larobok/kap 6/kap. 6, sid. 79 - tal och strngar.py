#!/usr/bin/python3.7

# Filnamn: kap. 6, sid. 79 - tal och strängar.py

# Kapitel 6 - Mer om teckensträngar i Python
# Programmering 1 med Python - Lärobok

# Strängar som innehåller tal
# Varje tecken i strängen lagras som en teckenkod och går inte att räkna med
string = '314'
print('string = ', string, ' -> ')
for c in range(len(string)):
    print('string[' + str(c) + '] = ' + string[c] + ', teckenkod: '+ str(ord(string[c])))

# För att beräkna måste strängen omvandlas till ett tal, obs går bara med heltal
number = int(string)
# number = int('123.45') # Genererar ett värdefel 
# ValueError: invalid literal for int() with base 10: '123.45'

# Omvandla tal till strängar
strHeltal = str(42)
strFlyttal = str(3.141592564)
strBool = str(False)
strUtfallVillkor = str(3 == 3)
strSträng = str('En liten sträng')

# Skriv ut alla variabler med omvandlade värden
print(strHeltal, strFlyttal, strBool, strUtfallVillkor, strSträng)

