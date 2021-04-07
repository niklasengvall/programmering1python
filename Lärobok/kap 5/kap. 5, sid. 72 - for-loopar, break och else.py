#!/usr/local/bin/python3.9

# Filnamn: kap. 5, sid. 72 - for-loopar, break och else.py

# Kapitel 5 - Loopar - upprepning, itteration
# Programmering 1 med Python - Lärobok

# Skriver ut alla primtal upp till 1000
for n in range(2, 1000):
    # Kolla om talet delbart med något tal
    # mindre än talet självt
    for d in range(2, n):
        # Blir det en rest så är det inget primtal
        if n % d == 0:
            break
    else:
        print(n, end=' ')