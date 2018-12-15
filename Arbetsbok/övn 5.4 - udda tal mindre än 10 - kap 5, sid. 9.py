#!/usr/bin/python3

# Filnamn: övn 5.4 - udda tal mindre än 10 - kap 5, sid 9.py

# Loopar - upprepning, iteration
# Programmeringsövningar till kapitel 5 - Arbetsbok

# Programmet skriver ut alla udda tal mindre än 10
for i in range(10): # Vi börjar med 0 i nästa itteration blir det 1 och
                    # fortsätter till 9
    if i % 2:   # Blir det rest då är det ett udda tal
        print(i, end = ' ')
print('')
input('\nTryck på en tangent...\n')
