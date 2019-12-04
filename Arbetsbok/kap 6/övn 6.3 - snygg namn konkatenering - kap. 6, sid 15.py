#!/usr/bin/python3.8

# Filnamn: övn 6.3 - snygg namn konkatenering - kap. 6, sid 15.py

# Mer om teckensträngar i Python
# Programmeringsövningar till kapitel 6

# Programmet frågar efter för- och efternamn och lägger dessa i en varsin 
# variabel, därefter slås dessa variabler ihop med ett mellanslag.
# Slutligen så formaterar vi alla inmatade ord med inledande versal

fnamn = input('Ange förnamn: ')
enamn = input('Ange efternamn: ')
namn = fnamn + ' ' + enamn
print(namn.title())
