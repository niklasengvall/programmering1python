#!/usr/local/bin/python3.9

# Filnamn: övn 5.9 - tabell med tal, kvadrater och kuber - kap 5, sid. 10.py

# Loopar - upprepning, iteration
# Programmeringsövningar till kapitel 5 - Arbetsbok

# Programmet skriver ut en tabell med de 20 första talen, dess kvadrater och 
# kub värden
# Skriv ut rubrik
print('Tal, kvadrater och kuber')
print('========================')

for i in range(1, 21):
    print('{0:>3d} {1:>4d} {2:>5d}'.format(i, i*i, i*i*i))

input('\nTryck på en tangent...\n')