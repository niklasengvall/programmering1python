#!/usr/local/bin/python3.9

# Filnamn: kap. 9, sid. 107 - funktioner.py

# Kapitel 9 - Funktioner
# Programmering 1 med Python - Lärobok

# Funktioner är egentligen återanvändbara små kodblock (programsnuttar) som kan 
# anropas om och om igen. För att använda och kunna anropa dessa kodblock så 
# måste de vara namngivna.

# Funktioner skapas nämligen genom att vi definierar dem med ett namn, därefter
#  kommer eventuellt en eller flera formella parametrar (ofta förkortat 
# parametar) inom parenteser. En funktion måste inte ha parametrar.
# Funktionsdefinitionen måste vara placerad så att den genomgåtts och sets av 
# Python-tolken innan anrop till den sker


# Exempel på funktion med tre parametrar som inte anropas och körs förrän 
# funktionen aropas i koden utanför. 
def skrivUtSumma(a, b, c):  # Funktionshuvud
    s = a + b + c
    print('Summan av de tre argumenten:', a,'och', b, 'samt', c, 'blev', s)

# Funktionsanrop, med 3 argument som kopieras till funktionens 3 parametrar
skrivUtSumma(3, 12, 9)  
x = 5
y = 7
z = 8
# Funktionsanrop, med 3 variabelreferenser som argument och som kopieras till 
# funktionens 3 parametrar
skrivUtSumma(x, y, z)
