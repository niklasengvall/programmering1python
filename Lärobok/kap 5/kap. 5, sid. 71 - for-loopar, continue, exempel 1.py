#!/usr/bin/python3.7

# Filnamn: kap. 5, sid. 71 - for-loopar, continue, exempel 1.py

# Kapitel 5 - Loopar - upprepning, itteration
# Programmering 1 med Python - Lärobok

# skriv ut alla jämna tal upp till 50 
for num in range(1,51):
    # Hoppa över alla udda tal
    if num % 2 == 1: # Modulo testar om vi får en rest 
        continue
    print(num, end = ', ')
