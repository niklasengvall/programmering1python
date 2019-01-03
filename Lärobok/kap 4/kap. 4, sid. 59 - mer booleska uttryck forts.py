#!/usr/bin/python3.7

# Filnamn: kap. 4, sid. 59 - mer booleska uttryck forts.py

# Kapitel 4 - Villkor, IF-satser
# Programmering 1 med Python - Lärobok

# några interaktiva exempel från boken omgjorda till program
# observera att jag bytt ut tal, variabler och villkor av respekt till
# författaren 
t1 = 3
t2 = 2
t3 = 1

if t1 > t2 or t2 > t3:
    print('t1 är större än t2 eller t2 är större än t3 eller så är bägge villkoren uppfyllda')

if t2 > t1 or t2 > t3:
    print('t2 är större än t1 eller t2 är större än t3 eller så är bägge villkoren uppfyllda')

# Tilldelning av booleska konstanter (True eller False)
t1 = True
if t1:
    print('t1 är True')

# Onödigt och ofta nybörjarfel då if-sats utgår från att alla positiva värden 
# i villkorsuttrycket är sant/True
if t1 == True:
    print('t1 är True')
