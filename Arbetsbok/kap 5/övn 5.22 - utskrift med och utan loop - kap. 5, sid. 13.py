#!/usr/local/bin/python3.9

# Filnamn: övn 5.22 - utskrift med och utan loop - kap. 5, sid. 13.py

# Programmet skriver ut fyra rader med 10 st asterisker med två olika metoder
# Metod 1: med for-loop
# Metod 2: med endast print-sats och escape-sekvenser

# Metod 1
for i in range(4):
    print('**********')

# Radmellanrum
print('')

# Metod 2
print("""**********\b
**********\b
**********\b
**********""")
