#!/usr/local/bin/python3.9

# Filnamn: kap. 6, sid. 76 - sätta ihop strängar.py

# Programmering 1 med Python - Lärobok
# Kapitel 6 - Mer om teckensträngar i Python

# Med plustecken kan du slå samman flera strängar till en enda.
# Det kallas även konkatenering av strängar
fn = 'Tage'
ln = 'Test'
name = fn + ln
print(name)

# Som du ser så skrivs inget mellanslag ut i den första print-satsen, 
# det måste du manuellt lägga in själv
name = fn + ' ' + ln
print(name)

# Upprepning av strängar görs med multiplikationstecknet *
print(3 * 'Hola!')
print(15 * '-')