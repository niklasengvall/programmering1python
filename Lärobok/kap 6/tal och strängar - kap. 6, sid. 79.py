#!/usr/bin/python3.7

# Filnamn: tal och strängar - kap. 6, sid. 79.py

# Programmering 1 med Python - Lärobok
# Kapitel 6 - Mer om teckensträngar i Python

# Strängar som innehåller tal
# Varje tecken i strängen lagras som en teckenkod och går inte att räkna med
s = '456'
print('s = ', s, ' -> ')
for i in range(len(s)):
    print('s[' + str(i) + '] = ' + s[i] + ', teckenkod: '+ str(ord(s[i])))

# För att beräkna måste strängen omvandlas till ett tal, obs går bara med heltal
tal = int(s)
# tal = int('123.45') # Genererar ett värdefel 
# ValueError: invalid literal for int() with base 10: '123.45'

# Omvandla tal till strängar
strHeltal = str(42)
strFlyttal = str(12.345)
strBool = str(True)
strUtfallVillkor = str(5 == 5)
strSträng = str('En sträng')

# Skriv ut alla variabler med omvandlade värden
print(strHeltal, strFlyttal, strBool, strUtfallVillkor, strSträng)

