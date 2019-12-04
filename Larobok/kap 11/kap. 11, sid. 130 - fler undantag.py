#!/usr/bin/python3.8

# Filnamn: kap. 11, sid. 130 - fler undantag.py

# Kapitel 11 - Felhantering i Python - undantag eller "Exceptions"
# Programmering 1 med Python - Lärobok

# Fler undantag

x = 20
# y = 2 # Vi tar bort en variabel för ett sk. NameError

try:
    z = x / y # Genererar ett division med noll fel
except ZeroDivisionError:
    print('Fel: Division med noll.')
# Ett nytt undantag görs med fler except
except NameError:
    print('Fel: Odefinierad variabel')
# Vad som ska ske om allt är ok skrivs efter else
else:
    print('Resultatet av divisionen:', z)

print('Här fortsätter vi programmet')
