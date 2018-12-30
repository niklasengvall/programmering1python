#!/usr/bin/python3

# Filnamn: sätta ihop strängar - kap. 6, sid. 76.py

# Programmering 1 med Python - Lärobok
# Kapitel 6 - Mer om teckensträngar i Python

# Med plustecken kan du slå samman flera strängar till en enda.
# Det kallas även konkatenering av strängar
fnamn = 'Eva'
enamn = 'Svensson'
namn = fnamn + enamn
print(namn)

# Som du ser så skrivs inget mellanslag ut i den första print-satsen, 
# det måste du manuellt lägga in själv
namn = fnamn + ' ' + enamn
print(namn)

# Upprepning av strängar görs med multiplikationstecknet *
print(5*'Hej')
print(5*'123')