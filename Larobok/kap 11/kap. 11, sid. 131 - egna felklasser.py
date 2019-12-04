#!/usr/bin/python3.8

# Filnamn: kap. 11, sid. 131 - egna felklasser.py

# Kapitel 11 - Felhantering i Python - undantag eller "Exceptions"
# Programmering 1 med Python - Lärobok

# Du kan ha egna namn på dina fel genom att definiera egna felklasser. Det är 
# rekommenderat att dessa klasser slutar på "Error"
class MinusError(Exception):
    pass

try:
    tal = int(input('Ange ett positivt heltal: '))
    if tal <= 0:
        raise MinusError
except MinusError:
    print('Fel: Tal måste vara större än noll.')
except ValueError:
    print('Fel: Det du angav är inget tal.')
except: 
    # Annat okänt fel
    print('Fel: Oväntat okänt fel.')
else:
    # Allt ok, inga fel, kör nedanstående
    z = 1 / tal

# Här kan det bli fel om inte else-satsen körts, z saknar värde
try:
    print('z = ',z)
except NameError:
    print('Fel: Vaiabel z är inte definierad, därför kan ingen utskrift ske.')