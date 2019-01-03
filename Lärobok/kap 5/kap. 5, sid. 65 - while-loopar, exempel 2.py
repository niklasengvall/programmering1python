#!/usr/bin/python3.7

# Filnamn: kap. 5, sid. 65 - while-loopar, exempel 2.py

# Kapitel 5 - Loopar - upprepning, itteration
# Programmering 1 med Python - Lärobok

# while-loop som räknare
# Loopen skriver ut namnet Ola tre gånger
# Därefter skrivs texten "Olé Olé Ola!"

r = 1
while r <= 3:
    print('Ola!')  
    r += 1

# Satsen nedan körs så fort loopens villkor inte uppfylls (blir falskt)
print('Olé Olé Ola!')