#!/usr/local/bin/python3.9

# Filnamn: övn 5.5 - summera alla tal- kap 5, sid 9.py

# Loopar - upprepning, iteration
# Programmeringsövningar till kapitel 5 - Arbetsbok

# Programmet summerar alla tal t.o.m. 50 
summa = 0   # Variabel som ska lagra totalsumman
for i in range(1, 51): # Vi börjar med 1 och ökar med tills vi når 50  
    summa += i
    print("i = " + str(i) + ", summa = " + str(summa))
print('')
input('\nTryck på en tangent...\n')
