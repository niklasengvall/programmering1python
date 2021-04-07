#!/usr/local/bin/python3.9

# Filnamn: övn 5.7 - vad skrivs ut- kap 5, sid 9.py

# Loopar - upprepning, iteration
# Programmeringsövningar till kapitel 5 - Arbetsbok

# Programmet skriver ut 3 st X och 4 st Y 
x = 0
for i in range(10):
    x = x + 1           # I första loopen ökar x med 1
    for j in range(10):
        x = x + 1       # I andra loopen ökar x med 10 => x = 11
    print(x)            # i första inre loop körning skrivs siffrorna 2 - 11 

print('')
input('\nTryck på en tangent...\n')

# På skärmen visas följande:
# 11 
# 22
# 33
# 44
# 55
# 66
# 77
# 88
# 99
# 110