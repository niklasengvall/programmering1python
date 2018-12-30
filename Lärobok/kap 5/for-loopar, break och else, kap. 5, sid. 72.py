#!/usr/bin/python3

# Filnamn: for-loopar, break och else, kap. 5, sid. 72.py

# Ett (inte särskilt effektivt) program som skriver ut 
# alla primtal upp till 100
for tal in range(2, 100):
    # Kolla om talet delbart med något tal
    # mindre än talet självt
    for div in range(2, tal):
        if tal % div == 0:
            break
    else:
        print(tal, end=' ')