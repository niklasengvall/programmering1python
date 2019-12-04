#!/usr/bin/python3.7

# Filnamn: kap. 9, sid. 108 - lokala och globala variabler.py

# Kapitel 9 - Funktioner
# Programmering 1 med Python - Lärobok

# Funktioners egna variabler är lokala och osynliga för koden utanför 
# funktionen. Variabler utanför funktionen kan ha samma namn som de som finns 
# innuti funktionen.

# Exempel på funktions lokala variabler och åtkomst då vi använder samma 
# variabelnamn såväl innom som utanför funktionen
# Notera också att funktionen saknar returvärde och kallas i andra programspråk,
# subrutin eller procedur
def enkelFunktion(z):
    print('z inom funktionen är först:', z)
    z **= 2 # kvadrera parameter z
    print('z inom funktionen är efter bearbetning:', z)

# Huvudprogram
z = 3 
print('z utanför funktionen är först:', z)
enkelFunktion(z) # z variablens värde, dvs. parametern kopieras till funktionen
print('z utanför funktionen är efter funktionsanrop:', z)
# Notera vad z är efter funktionsanrop, orsak är att z i huvudprogram och i 
# funktion är helt difrentierade och refererar till olika lagringsplatser i 
# minnet