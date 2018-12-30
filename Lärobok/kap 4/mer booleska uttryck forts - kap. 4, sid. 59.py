#!/usr/bin/python3

# Filnamn: mer booleska uttryck forts - kap. 4, sid. 59.py

# några interaktiva exempel omgjorda till program

a = 5
b = 6
c = 7
d = 7

if a < b or b < c:
    print('a är mindre än b eller b är mindre än c (eller både och)')
if b < a or b < c:
    print('b är mindre än a eller b är mindre än c (eller både och)')

# Tilldelning av booleska konstanter (True eller False)
a = True
if a:
    print('a är sant')

# Onödigt och ofta nybörjarfel
if a == True:
    print('a är sant')
