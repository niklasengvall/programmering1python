#!/usr/bin/python3.7

# Filnamn: övn 6.12 - hur mår du - kap. 6, sid. 17.py

# Mer om teckensträngar i Python
# Programmeringsövningar till kapitel 6

# Programmet frågar hur du mår och ger olika svar beroende på vad du skriver

# Flaggor för positivt eller negativa ord i svar
positivt = False
negativt = False

# Ställ fråga
svar = input('Hur mår du? : ')

# Ändra svaret till gemener vilket innebär förenklad vilkorskontroll
svar = svar.lower()

# Om svaret innehåller bra eller fint så är det positivt
if 'bra' in svar:
    positivt = True
elif 'fint' in svar:
    positivt = True

# Om svaret innehåller dåligt eller illa så är det negativt
if 'dåligt' in svar:
    negativt = True
elif 'illa' in svar:
    negativt = True

# Om svaret innehåller inte  och bra så är det negativt
if 'inte' in svar:
    if 'bra' in svar:
        positivt = False
        negativt = True 

if positivt:
    print('Det var roligt att höra')
elif negativt:
    print('Det var tråkigt')
else:
    print('Eh, jag förstår inte?')