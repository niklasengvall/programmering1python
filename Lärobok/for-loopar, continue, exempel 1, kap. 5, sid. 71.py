#!/usr/bin/python3

# Filnamn: for-loopar, continue, exempel 1, kap. 5, sid. 71.py

# Loopa igenom och skriv ut alla jämna tal 
for tal in range(100):
    # Hoppa över alla udda tal
    if tal % 2 == 1:
        continue
    print(tal, end = ' ')
