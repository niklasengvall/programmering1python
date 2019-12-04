#!/usr/bin/python3.7

# Filnamn: kap. 4, sid. 55 - demonstration av if-satser.py

# Kapitel 4 - Villkor, IF-satser
# Programmering 1 med Python - Lärobok

# if-satser
# Först initierar vi några variabler som vi sedan kan testa på
a = 9
b = 6
c = 3

# Enkla jämförelser
# Villkorstest med mindre än och större än
if b < a:
    print('b är mindre än a')
if a > b:
    print('a är större än b')

# Villkorstest av större än eller lika med
if b >= c:
    print('b är större än eller lika med c')

# Vilkorstest på likhet samt nästling av if-satser 
# (if-sats i if-sats)
c = 9
if c == a:
    print('c är lika med a')
    print('Dessa rader hör också till')
    print('if-blocket som sagt')
    if c > b:
        print('Och är c större än b')
        print('Dessutom ser vi här exempel på if-satser i if-satser')

# Test för olikhet
if c != 7:
    print('c är inte lika med 7')
