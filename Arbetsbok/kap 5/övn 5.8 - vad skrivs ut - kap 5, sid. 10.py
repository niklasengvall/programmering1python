#!/usr/bin/python3.7

# Filnamn: övn 5.8 - vad skrivs ut- kap 5, sid 10.py

# Loopar - upprepning, iteration
# Programmeringsövningar till kapitel 5 - Arbetsbok

# Programmet skriver ut 3 st X och 4 st Y 
x = 0
for i in range(10):
    x = x + 1           # I första loopen ökar x med 1
    for j in range(10):
        x = x + 1       # I andra loopen ökar x med 10 => x = 11
print(x)                # skriv ut vad x innehåller efter att alla loopar körts

print('')
input('\nTryck på en tangent...\n')

# På skärmen visas följande:
# 110